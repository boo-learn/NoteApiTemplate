import os

os.environ["DATABASE_URI"] = 'sqlite:///:memory:'
from api import db
from app import app
from base64 import b64encode
from api.models.user import UserModel
import pytest


@pytest.fixture()
def application():
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()


@pytest.fixture()
def client(application):
    return application.test_client()


@pytest.fixture()
def user_admin():
    user_data = {"username": "admin", "password": "admin", "role": "admin"}
    user = UserModel(**user_data)
    user.save()
    return user


@pytest.fixture()
def auth_headers(user_admin):
    user_data = {"username": "admin", "password": "admin", "role": "admin"}
    headers = {
        'Authorization': 'Basic ' + b64encode(
            f"{user_data['username']}:{user_data['password']}".encode('ascii')).decode('utf-8')
    }
    return headers
