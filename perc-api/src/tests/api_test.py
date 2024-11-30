import pytest
from src.app import create_app

@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()

def test_request_example(client):
    response = client.get("/v1/get-token")
    print(response.json['data']['recommendations'])
    assert len(response.json['data']['recommendations'])>0

@pytest.fixture()
def runner(app):
    return app.test_cli_runner()