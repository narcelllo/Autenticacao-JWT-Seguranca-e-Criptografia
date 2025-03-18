import pytest
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from .user_register_view import UserRegisterView

class MockController:
    def registry(self, username, password):
        return {"info": "mock"}

def test_handle_user_register():
    body = {
        "username": "UsernameTest",
        "password": "passwordTeste"
    }
    request = HttpRequest(body=body)

    mock_controller = MockController()
    user_register_view = UserRegisterView(mock_controller)

    response = user_register_view.handle(request)
    #print()
    #print(response.body)
    assert response.body == {'data': {'info': 'mock'}}
    assert response.status_code == 201
    assert isinstance(response, HttpResponse)

def test_handle_user_register_error():
    body = {
        "username": "UsernameTest"
    }
    request = HttpRequest(body=body)

    mock_controller = MockController()
    user_register_view = UserRegisterView(mock_controller)

    with pytest.raises(Exception):
        user_register_view.handle(request)

def test_handle_user_register_error_int():
    body = {
        "username": "UsernameTest",
        "password": 123
    }
    request = HttpRequest(body=body)

    mock_controller = MockController()
    user_register_view = UserRegisterView(mock_controller)

    with pytest.raises(Exception):
        user_register_view.handle(request)