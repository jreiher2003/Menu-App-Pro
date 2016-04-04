import unittest 
from base import BaseTestCase 
from app import app,db 
from flask import request
from app.models import Place, Menu

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
        assert place.address == "123 Test st."
        assert place.city == "Englewood"
        assert place.state == "Florida"
        assert place.zip_ == "34224"
        assert place.website == "http://fake.com"
        assert place.phone == "123-456-7899"
        assert place.owner == "Jeff Reiher"
        assert place.yrs_open == 1

    def test_menu_database(self):
        menu = Menu.query.filter_by(id=1).one()
        assert menu.name == "burger"
        assert menu.course == "dinner"
        assert menu.description == "test description"
        assert menu.price == "$1.00"

    def test_request_url(self):
        with app.test_request_context("/", method="GET"):
            assert request.path == "/"
            assert request.method == "GET"

    def test_create_new_restaurant(self):
        response = self.client.get("/restaurant/new")
        assert response.status_code == 200

    def test_place_name(self):
        response = self.client.get("/restaurant/1/menu")
        assert response.status_code == 200

    def test_place_edit(self):
        response = self.client.get("/restaurant/1/edit")
        assert response.status_code == 200

    def test_place_delete(self):
        response = self.client.get("/restaurant/1/delete")
        assert response.status_code == 200

    def test_create_new_menu_item(self):
        response = self.client.get("/restaurant/1/new")
        assert response.status_code == 200

    def test_menu_edit(self):
        response = self.client.get("/restaurant/1/menu/1/edit")
        assert response.status_code == 200

    def test_menu_delete(self):
        response = self.client.get("/restaurant/1/menu/1/delete")
        assert response.status_code == 200




    

            




