def test_create_user(client, user_data):
    resp = client.post(
        '/user/register',
        json=user_data.dict()
    )
    assert resp.status_code == 201


def test_user_exists(client, user_data):
    url = '/user/register'
    client.post(url, json=user_data.dict())
    resp = client.post(url, json=user_data.dict())
    assert resp.status_code == 409
    assert resp.json()['detail'] == 'A User with this email already exists'
