import pytest
import requests
from requests.auth import HTTPBasicAuth


@pytest.fixture(scope="class")
def session():
    session = requests.Session()

    auth_response = session.post(
        "http://127.0.0.1:8080/auth",
        auth=HTTPBasicAuth("test_user", "test_pass")
    )

    assert auth_response.status_code == 200, (
        f"Authentication failed: {auth_response.text}"
    )

    access_token = auth_response.json()["access_token"]

    session.headers.update({
        "Authorization": f"Bearer {access_token}"
    })

    yield session

    session.close()
