from flask import url_for


class TestPage(object):
    def test_index_page(self, client):
        response = client.get('/')
        assert response.status_code == 200

    def test_contact_page(self, client):
        response = client.get(url_for('page.contact'))
        assert response.status_code == 200

    def test_privacy_page(self, client):
        response = client.get(url_for('page.privacy'))
        assert response.status_code == 200

    def test_not_found_page(self, client):
        response = client.get('/hello')
        assert response.status_code == 404
