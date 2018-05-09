from flask import json


class TestUser(object):
    def test_get_user(self, client):
        response = client.get('/user/api')
        data = json.loads(response.data)  # loads response as a dict
        assert response.status_code == 200
        assert data['email'] == 'ken@yahoo.com'
