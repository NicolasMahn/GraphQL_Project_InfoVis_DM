import os
from urllib.parse import quote_plus

# MongoDB connection details
username = quote_plus(os.getenv("MONGODB_USERNAME").encode('utf-8'))
password = quote_plus(os.getenv("MONGODB_PASSWORD").encode('utf-8'))
aws_dns = os.getenv("AWS_DNS")
mongodb_port = os.getenv("MONGODB_PORT")
mongodb_name = os.getenv("MONGODB_NAME")

MONGO_URI = f"mongodb://{username}:{password}@{aws_dns}:{mongodb_port}"
MONGO_DB_NAME = mongodb_name

GRAPHQL_SERVER_PORT = os.getenv("GRAPHQL_SERVER_PORT")
DEBUG_MODE = os.getenv("DEBUG_MODE")