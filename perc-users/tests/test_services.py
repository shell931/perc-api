import pytest
from services.UserService import CreateUser, GetAllUser, SearchUsers

def test_create_user():
    """Test CreateUser service."""
    http_code, name, username, email, message = CreateUser(
        name="John Doe",
        username="jdoe",
        email="john.doe@example.com"
    )
    assert http_code == 201
    assert name == "John Doe"
    assert username == "jdoe"
    assert email == "john.doe@example.com"
    assert message == "User created success"
    
def test_get_all_users(mocker):
    """Test GetAllUser service with mocked response."""
    mock_response = [
        {
            "name": "John Doe",
            "address": {"city": "Sample City"},
            "company": {"name": "Sample Company"}
        }
    ]
    mocker.patch("requests.get", return_value=mocker.Mock(status_code=200, json=lambda: mock_response))
    
    http_code, users = GetAllUser()
    assert http_code == 200
    assert len(users) == 1
    assert users[0]["name"] == "John Doe"
    
def test_search_users(mocker):
    """Test SearchUsers service with mocked response."""
    mock_response = [
        {"name": "Alice", "address": {"city": "Wonderland"}, "company": {"name": "Rabbit Inc."}},
        {"name": "Bob", "address": {"city": "Builderland"}, "company": {"name": "Construction Ltd."}},
    ]
    mocker.patch("requests.get", return_value=mocker.Mock(status_code=200, json=lambda: mock_response))
    
    mock_request = type("Request", (object,), {
        "name": "Alice",
        "city": "",
        "company_name": "",
        "order_by": "name",
        "desc": False
    })
    
    http_code, users = SearchUsers(mock_request)
    assert http_code == 200
    assert len(users) == 1
    assert users[0]["name"] == "Alice"