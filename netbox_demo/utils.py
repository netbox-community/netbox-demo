import string
import random

from django.contrib.auth import get_user_model


def generate_username():
    unique_id = random.randrange(999999)
    return f'user{unique_id}'


def generate_password(length=8):
    character_pool = string.ascii_letters + string.digits
    chars = [
        random.choice(character_pool) for i in range(length)
    ]
    return ''.join(chars)


def create_user(username=None, password=None, **kwargs):
    """
    Automatically create a new demo user account. Returns the User instance and plaintext password.
    """
    if username is None:
        username = generate_username()
    if password is None:
        password = generate_password()

    User = get_user_model()
    user = User.objects.create_superuser(username=username, password=password, **kwargs)

    return user, password
