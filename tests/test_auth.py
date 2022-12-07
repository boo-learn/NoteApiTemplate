import pytest
from api.models.user import UserModel
from api.models.note import NoteModel
from tests.init_test import client, user_admin, application, auth_headers


def test_basic_auth(client, auth_headers, user_admin):
    response = client.get('/auth/token', headers=auth_headers)
    data = response.json
    assert response.status_code == 200
    assert data["token"] == user_admin.generate_auth_token()


@pytest.mark.skip(reason="test not implemented")
def test_token_auth(client):
    pass
    # Пока отложим реализацию данного теста
