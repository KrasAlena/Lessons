# test_token_access.py
from Ex_1 import UserVerificationApp


def test_verified_user_gets_token():
    # Initialize the application
    app = UserVerificationApp()

    # The customer has the following username and password
    username = "alice"
    password = "pass123"

    # The customer inputs valid username and password to register new user
    app._register_user(username, password)

    # The user verifies the newly created user
    app._verify_user(username, password)

    # The user generates a token for the newly created and verified user
    token = app._generate_token(username)
    assert token is not None


def test_unverified_user_does_not_get_token():
    # Initialize the application
    app = UserVerificationApp()

    # The customer inputs valid username and password to register new user
    username = "alice"
    password = "pass123"

    # The customer inputs valid username and password to register new user
    app._register_user(username, password)

    # (The customer forgets to verify their newly created user)

    # The customer tries to generate a token for the newly created and verified user
    # and fails
    token = app._generate_token(username)
    assert token is None


def test_registered_user_with_wrong_username():
    # Initialize the application
    app = UserVerificationApp()

    # The customer inputs valid username and password to register new user
    username = "alice"
    password = "pass123"

    # The customer inputs valid username and password to register new user
    app._register_user(username, password)

    #  The newly created user tries to verify with invalid username and valid password
    app._verify_user('alic', password)
    # The customer tries to generate a token for the newly created and verified user
    # and fails
    token = app._generate_token(username)
    assert token is None


def test_registered_user_with_wrong_password():
    # Initialize the application
    app = UserVerificationApp()

    # The customer inputs valid username and password to register new user
    username = "alice"
    password = "pass123"

    # The customer inputs valid username and password to register new user
    app._register_user(username, password)

    #  The newly created user tries to verify with valid username and invalid password
    app._verify_user(username, 'pas123')

    # The customer tries to generate a token for the newly created and verified user
    # and fails
    token = app._generate_token(username)
    assert token is None


def test_verifying_user_which_not_exist():
    # Initialize the application
    app = UserVerificationApp()

    # (The user forgets to register before verifying)

    #  The user tries to verify with unregistered username and password
    app._verify_user('mess', 'qwerty1')

    # The customer tries to generate a token for the newly created and verified user
    # and fails
    token = app._generate_token('mess')
    assert token is None


def test_verified_user_tries_to_get_token_with_wrong_and_valid_username():
    # Initialize the application
    app = UserVerificationApp()

    # The customer has the following username and password
    username = "alice"
    password = "pass123"

    # The customer inputs valid username and password to register new user
    app._register_user(username, password)

    # The user verifies the newly created user
    app._verify_user(username, password)

    # The user generates a token for a user that does not exist
    token = app._generate_token('alicia')
    assert token is None

    # Then the user generates a token with valid username
    token = app._generate_token('alice')
    assert token is not None

'''
The user of the program registers three users, verifies only the first one, 
tries to generate a token for the second one and fails, tries to generate 
a token for the first one and succeeds, then verifies the second user, 
tries to generate a token for the second one again and succeeds.
'''
def test_tree_users_verified_only_first():
    # Initialize the application
    app = UserVerificationApp()

    # The customer has the following username and password
    username1 = "alice"
    password1 = "pass123"

    username2 = "mark"
    password2 = "pass456"

    username3 = "ann"
    password3 = "pass789"

    # The customer inputs valid username and password to register new user
    app._register_user(username1, password1)
    app._register_user(username2, password2)
    app._register_user(username3, password3)

    # The user verifies the newly created user
    app._verify_user(username1, password1)

    # The user generates a token for the newly created and verified user
    token = app._generate_token(username2)
    assert token is None

    token = app._generate_token(username1)
    assert token is not None

    app._verify_user(username2, password2)