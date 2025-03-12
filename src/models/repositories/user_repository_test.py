from src.models.settings.db_connection_handler import db_connection_handler
from .user_repository import UserRepository
from unittest.mock import Mock

class MockCursor:
    def __init__(self) -> None:
        self.execute = Mock()
        self.fetchone = Mock()

class MockConnection:
    def __init__(self) -> None:
        self.cursor = Mock(return_value=MockCursor())
        self.commit = Mock()

def test_repository_user():
    username = "name"
    password = "heuh"

    mock_connection = MockConnection()
    repo = UserRepository(mock_connection)
    repo.registry_user(username, password)

    cursor = mock_connection.cursor.return_value
    #print()
    #print(cursor.execute.call_args[0])

    assert "INSERT INTO users" in cursor.execute.call_args[0][0]
    assert "(username, password, balance)" in cursor.execute.call_args[0][0]
    assert "VALUES" in cursor.execute.call_args[0][0]
    assert "(?, ?, ?)" in cursor.execute.call_args[0][0]
    assert cursor.execute.call_args[0][1] == (username, password, 0)

def test_edit_balance():
    balance = 123.65
    user_id = 2

    mock_connection = MockConnection()
    repo = UserRepository(mock_connection)

    repo.edit_balance(balance, user_id)

    cursor = mock_connection.cursor.return_value
    #print()
    #print(cursor.execute.call_args[0])

    assert "UPDATE users" in cursor.execute.call_args[0][0]
    assert "SET balance = ?" in cursor.execute.call_args[0][0]
    assert "WHERE id = ?" in cursor.execute.call_args[0][0]
    assert cursor.execute.call_args[0][1] == (user_id, balance)

def test_get_user_by_username():
    username = "username"

    mock_connection = MockConnection()
    repo = UserRepository(mock_connection)

    repo.get_user_by_username(username)

    cursor = mock_connection.cursor.return_value
    #print()
    #print(cursor.execute.call_args[0])

    assert "SELECT id, username, password" in cursor.execute.call_args[0][0]
    assert "FROM users" in cursor.execute.call_args[0][0]
    assert "WHERE username = ?" in cursor.execute.call_args[0][0]
    assert cursor.execute.call_args[0][1] == (username,)

