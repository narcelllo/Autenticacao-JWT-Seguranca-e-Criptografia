import pytest
from .user_repository import UserRepository
from src.models.settings.db_connection_handler import db_connection_handler

@pytest.mark.skip("Insert in DB")
def test_repository():
    db_connection_handler.connect()
    conn = db_connection_handler.get_connection()
    repo = UserRepository(conn)

    username = "NameTest2"
    password = "password1235"

    repo.registry_user(username, password)
    user = repo.get_user_by_username(username)
    print()
    print(user)
    #print(user[0])
    #print(user[1])
    repo.edit_balance(user[0], 7894.56)
    user1 = repo.get_user_by_username(username)
    print()
    print(user1)