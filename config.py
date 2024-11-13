import os
from urllib.parse import quote_plus




# MongoDB connection details
username = quote_plus(os.getenv("MONGODB_USERNAME"))
password = quote_plus(os.getenv("MONGODB_PASSWORD"))
AWS_DNS = os.getenv("AWS_DNS")
mongodb_port = os.getenv("MONGODB_PORT")
mongodb_name = os.getenv("MONGODB_NAME")

MONGO_URI = f"mongodb://{username}:{password}@{AWS_DNS}:{mongodb_port}"
MONGO_DB_NAME = mongodb_name

GRAPHQL_SERVER_PORT = os.getenv("GRAPHQL_SERVER_PORT")