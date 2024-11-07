import pytest
import requests
from app import app  # Import the Flask app

# Use pytest fixture to set up and tear down the app context
@pytest.fixture
def client():
    # Configure the app for testing
    app.config["TESTING"] = True
    app.config["DEBUG"] = False

    # Start the app in test mode
    with app.test_client() as client:
        yield client

# Test to check the GraphQL endpoint
def test_graphql_endpoint(client):
    # Define the query to test
    query = {
        "query": "{ people { name age } }"
    }

    # Make a request to the /graphql endpoint
    response = client.post("/graphql", json=query)

    # Check that the response has status code 200 (OK)
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"

    # Parse the JSON response
    data = response.get_json()

    # Check that data is in the expected format (assuming 'people' field exists)
    assert "data" in data, "Response missing 'data' field"
    assert "people" in data["data"], "Response missing 'people' field"

    # Additional optional checks (e.g., checking for specific names)
    people = data["data"]["people"]
    assert isinstance(people, list), "Expected 'people' to be a list"
    if people:
        assert "name" in people[0] and "age" in people[0], "People objects missing 'name' or 'age' fields"
