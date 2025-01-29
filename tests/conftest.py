

import pytest
import sys
import os

# Add the project root directory to the PYTHONPATH for module discovery
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.create_app import create_app  # Now this should work

@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    return app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def authenticated_client(client):
    # Simulate an authenticated request by adding a mocked token in the headers
    headers = {
        "Authorization": "Bearer mocked_valid_token"  # Replace with your actual token structure
    }
    client.environ_base['HTTP_AUTHORIZATION'] = headers['Authorization']
    return client
@pytest.fixture(scope="session", autouse=True)
def set_testing_env():
    os.environ['FLASK_ENV'] = 'testing'