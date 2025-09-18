from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
import pandas as pd
from airflow.hooks.postgres_hook import PostgresHook

# Default args
default_args = {
    'owner': 'data_eng',
    'depends_on_past': False,
    'retries': 1,
}

# DAG definition
with DAG(
    dag_id='postgres_etl_daily',
    default_args=default_args,
    start_date=days_ago(1),
    schedule='@daily',
    catchup=False,
    tags=['example', 'etl']
) as dag:

    # Step 1: Extract from PostgreSQL
    def extract_data(**kwargs):
        pg_hook = PostgresHook(postgres_conn_id='postgres_source')
        sql = "SELECT customer_id, order_date, total_amount FROM orders"
        df = pg_hook.get_pandas_df(sql)
        # Push data to XCom
        kwargs['ti'].xcom_push(key='orders_df', value=df.to_json())

    extract_task = PythonOperator(
        task_id='extract_orders',
        python_callable=extract_data,
        provide_context=True
    )

    # Step 2: Transform in Python
    def transform_data(**kwargs):
        import json
        ti = kwargs['ti']
        orders_json = ti.xcom_pull(key='orders_df', task_ids='extract_orders')
        df = pd.read_json(orders_json)
        # Calculate total per customer
        df_summary = df.groupby('customer_id')['total_amount'].sum().reset_index()
        df_summary.rename(columns={'total_amount': 'total_sales'}, inplace=True)
        ti.xcom_push(key='orders_summary', value=df_summary.to_json())

    transform_task = PythonOperator(
        task_id='transform_orders',
        python_callable=transform_data,
        provide_context=True
    )

    # Step 3: Load into PostgreSQL
    def load_data(**kwargs):
        import json
        ti = kwargs['ti']
        df_json = ti.xcom_pull(key='orders_summary', task_ids='transform_orders')
        df = pd.read_json(df_json)

        pg_hook = PostgresHook(postgres_conn_id='postgres_target')
        conn = pg_hook.get_conn()
        cursor = conn.cursor()

        # Create target table if not exists
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS customer_sales_summary (
                customer_id INT PRIMARY KEY,
                total_sales NUMERIC
            )
        """)
        conn.commit()

        # Upsert data
        for _, row in df.iterrows():
            cursor.execute("""
                INSERT INTO customer_sales_summary (customer_id, total_sales)
                VALUES (%s, %s)
                ON CONFLICT (customer_id)
                DO UPDATE SET total_sales = EXCLUDED.total_sales
            """, (row['customer_id'], row['total_sales']))
        conn.commit()
        cursor.close()
        conn.close()

    load_task = PythonOperator(
        task_id='load_customer_summary',
        python_callable=load_data,
        provide_context=True
    )

    # DAG dependencies
    extract_task >> transform_task >> load_task
