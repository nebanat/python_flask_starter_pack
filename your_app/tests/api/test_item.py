from flask import json


class TestItem(object):
    def test_get_items(self, client):
        response = client.get('/items/api')
        data = json.loads(response.data)  # loads response as a dict
        assert response.status_code == 200
        assert data['message'] == 'items successfully fetched'
        assert type(data['items']) is list

    def test_get_single_item(self, client):
        response = client.get('/items/api/1')
        assert response.status_code == 200
