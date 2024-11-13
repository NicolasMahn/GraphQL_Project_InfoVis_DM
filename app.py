from flask_graphql import GraphQLView
from flask import Flask, jsonify
from flask_cors import CORS

from config import GRAPHQL_SERVER_PORT
from graph.schema import schema


app = Flask(__name__)

CORS(app, origins=["http://localhost:3000", "https://your-frontend-domain.com"])

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True  # Enables GraphiQL UI for testing
    )
)

@app.route('/')
def index():
    return jsonify({"message": "Welcome to the GraphQL API of the InvoVis & DM project!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=GRAPHQL_SERVER_PORT)
