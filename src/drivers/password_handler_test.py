from .password_handler import PasswordHandler

def test_encript():
    password = "123teste!@#"
    password_handler = PasswordHandler()

    hashed_password = password_handler.encrypt_password(password)
    #print()
    #print(hashed_password)

    password_checked = password_handler.check_password(password, hashed_password)
    #print()
    #print(password_checked)

    assert password_checked