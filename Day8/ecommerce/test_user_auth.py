from user_auth import UserAuth

auth=UserAuth()

def test_register_login():
    assert auth.register("user1","pass1")==True
    assert auth.login("user1","pass1")==True

def test_register_existing_user():
    assert auth.register("admin","pasword123")==False

def test_login_wrong_password():
    auth.register("user2","pass2")
    assert auth.login("user2","wrongpass")==False