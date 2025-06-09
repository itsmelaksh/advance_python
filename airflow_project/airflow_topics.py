"""
1. workflow/dags
2. Operators (BashOperator, PythonOperator, FileOperator, EmailOperator)
3. Tasks
4. Dependencies / Bitshift Operator
5. Sensors
6. Scheduling
    power templating, branching, debug, sla, provide_context etc 

airflow sensors

airflow executors
    sequentialexeuctor
    localexecutor
    kubernetesexecutor

    mode - reschedule, poke

airflow templates

    variables
        ds - date of run
        ds_nodash - date of run without dash yyyymmdd
        dag - gives dag info
        prev_ds - previous date of run
        prev_ds_nodash
        conf - configuration for the run
        macros - it gives macros.datetime etc
        for more variables : https://airflow.apache.org/docs/stable/macros-ref.html

branching


"""