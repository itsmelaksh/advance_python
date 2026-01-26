SELECT *
FROM {{ source('looker_ecommerce', 'events') }}

# similarly create for all the tables mentioned in _looker_sources.yml under looker_ecommerce
