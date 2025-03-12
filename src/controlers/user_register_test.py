from src.controlers.user_register import UserRegister

class MockUserRepository:
    def __init__(self) -> None:
        self.registry_user_attributes = {}

    def registry_user(self, username: str, password: str) -> None:
        self.registry_user_attributes["username"] = username
        self.registry_user_attributes["password"] = password


def test_registry():
        repository = MockUserRepository()
        controller = UserRegister(repository)

        username = "userTest"
        password = "passwordTest"

        response = controller.registry(username, password)
        #print()
        #print(response)
        #print(repository.registry_user_attributes)

        assert response["type"] == "User"
        assert response["username"] == username

        assert repository.registry_user_attributes["username"] == username
        assert repository.registry_user_attributes["password"] is not None
        assert repository.registry_user_attributes["password"] != password