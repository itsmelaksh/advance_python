Welcome to your new dbt project!

### Using the starter project

Try running the following commands:
- dbt run
- dbt test


### Resources:
- Learn more about dbt [in the docs](https://docs.getdbt.com/docs/introduction)
- Check out [Discourse](https://discourse.getdbt.com/) for commonly asked questions and answers
- Join the [chat](https://community.getdbt.com/) on Slack for live discussions and support
- Find [dbt events](https://events.getdbt.com) near you
- Check out [the blog](https://blog.getdbt.com/) for the latest news on dbt's development and best practices


# process
1. create directory in model directory 
2. create a .sql file in above directory 
3. Add sql statments in this file 
4. Run - dbt run 
Note - newer version of dbt can support python 


# creating dbt project documentation
- benefits
1. Easy to share the details 
2. documentation can be centralized for future understanding and kt
3. provides future reference for the changes made
4. Document minute level information to increase the understanding
- dbt docs 
1. easy to generate using - dbt docs generate 
2. dbt docs -h for help  
3. dbt docs serve - to access documentation using web server


# Using jinja template in creating sql 

select
{% for column_name in ['fare_amount', 'tip_amount', 'tolls_amount', 'total_amount'] %}
  {{column_name}}{% if not loop.last %},{% endif %}
{% endfor %}
from taxi_rides_raw

converted into
select fare_amount, tip_amount, tolls_amount, total_amount
from taxi_rides_raw

# hierarchical models


