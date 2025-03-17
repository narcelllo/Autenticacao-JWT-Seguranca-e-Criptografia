from src.models.interface.user_repository import UserRepositoryInterface
from src.drivers.jwt_handler import JwtHandler
from src.drivers.password_handler import PasswordHandler
from .interfaces.login_creator import LoginCreatorInterface

class LoginCreator(LoginCreatorInterface):
    def __init__(self, user_repostory: UserRepositoryInterface) -> None:
        self.__user_repository = user_repostory
        self.__jwt_handler = JwtHandler()
        self.__password_handler = PasswordHandler()

    def create(self, username : str, password: str) -> dict:
        user = self.__faind_user(username)
        user_id = user[0]
        hashed_password = user[2]

        self.__verify_correct_password(password, hashed_password)
        token = self.__create_jwt_token(user_id)
        return self.__format_response(username, token)

    def __faind_user(self, username: str, ) -> tuple[int, str, str]:
        user = self.__user_repository.get_user_by_username(username)
        if not user: raise Exception("user not found")

        return user
    
    def __verify_correct_password(self, password: str, hashed_password: str) -> None:
        correct_password = self.__password_handler.check_password(password, hashed_password)
        if not correct_password: raise Exception("Wrong password")

    def __create_jwt_token(self, user_id: int) -> str:
        payload = { "user_id": user_id }
        token = self.__jwt_handler.create_jwt_token(payload)
        return token
    
    def __format_response(self, username: str, token: str) -> dict:
        return {
            "access":True,
            "username": username,
            "token": token
        }