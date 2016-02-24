import unittest 
from base import BaseTestCase 
from app import app,db 
from flask import request
from app.models import Place

class TestFrontPage(BaseTestCase):

    def test_index_loads(self):
        response = self.client.get("/", follow_redirects=True)
        assert response.status_code == 200
        assert "Testname" in response.data

    def test_stylesheet_loads(self):
        response = self.client.get("/static/styles.css")
        assert response.status_code == 200

    def test_place_database(self):
    	place = Place.query.filter_by(id=1).one()
    	assert place.id == 1
        assert place.name == "Testname"

    def test_request_url(self):
        with app.test_request_context("/", method="GET"):
            assert request.path == "/"
            assert request.method == "GET"


    

            




