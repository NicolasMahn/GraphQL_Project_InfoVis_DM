from urllib.parse import quote_plus
import s

# MongoDB connection details
MONGO_URI = f"mongodb://{quote_plus(s.mongodb_username)}:{quote_plus(s.mongodb_password)}@{s.aws_dns}:{s.mongodb_port}"
MONGO_DB_NAME = s.mongodb_name

# Flask server configuration
SERVER_PORT = 5000
DEBUG_MODE = True
