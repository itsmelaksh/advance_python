import pandas as pd
import sqlalchemy

# Create a connection to the reviews database
db_engine = sqlalchemy.create_engine("postgresql+psycopg2://repl:password@localhost:5432/disneyland")

# Execute a query against the nested_reviews table
results = pd.read_sql("SELECT * FROM nested_reviews;", db_engine)
print(results)


"""
# Build a query to create a JSON-object
query = """
SELECT
	row_to_json(row(review_id, rating, year_month))
FROM reviews;
"""

# Execute the query, and output the results
results = pd.read_sql(query, db_engine)
print(results.head(10))


query = """
SELECT
	distinct json_object_keys(review)
FROM nested_reviews;
"""

# Execute the query, show the results
unique_keys = pd.read_sql(query, db_engine)
print(unique_keys)

"""

# json_extract_path #> and json_extract_path_text #>>
# Attempt to query the statement, nested branch, and nested
# zipcode fields from the review column
query = """
	SELECT 
    	json_typeof(review #> '{statement}'),
        review #> '{location, branch}' AS branch,
        review #> '{location, zipcode}' as zipcode
    FROM nested_reviews;
"""

# Execute the query, render results
data = pd.read_sql(query, db_engine)
print(data)

# Extract fields from JSON, and filter by reviewer location
query = """
    SELECT
    	review_id,
        review #> '{location, branch}' AS branch,
        review ->> 'statement' AS statement,
        rating
    FROM nested_reviews
    WHERE json_extract_path_text(review, 'location', 'reviewer') = 'Australia'
    ORDER BY rating DESC;
"""

data = pd.read_sql(query, db_engine)
print(data)
