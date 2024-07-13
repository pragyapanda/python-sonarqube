from app.utils import greet_user

def test_greet_user():
    assert greet_user("John") == "Hello, John!"
    assert greet_user("") == "Hello, !"
