from app import app,db # pragma: no cover
from app.models import Place, Menu # pragma: no cover
from flask import render_template # pragma: no cover

@app.route("/") 
@app.route("/restaurants")
def index(): 
	all_places = Place.query.all()
	return render_template('index.html', 
		all_places=all_places)

@app.route("/restaurant/new")
def create_new_place():
	return "this page is for making a new restaurant"

@app.route("/restaurant/<int:place_id>/edit")
def place_edit(place_id):
	return "this page will be for editing restaurant %s" % place_id

@app.route("/restaurant/<int:place_id>/delete")
def place_delete(place_id):
	return "this page will be for deleting restaurant %s" % place_id
	
@app.route("/restaurant/<int:place_id>/menu")
@app.route("/restaurant/<int:place_id>")
def place_menu(place_id):
	# place = Place.query.filter_by(id = place_id).one()
	# menuitems = Menu.query.filter(Menu.place_id == place_id).all()
	# return render_template("menu.html", 
	# 	place=place,
	# 	menuitems=menuitems)
	return "This page is the menu for restaurant %s" % place_id

@app.route("/restaurant/<int:place_id>/new")
def create_new_menu_item(place_id):
	return "This page is for making a new menu item for restaurant %s" % place_id

@app.route("/restaurant/<int:place_id>/menu/<int:menu_id>/edit")
def edit_menu_items(place_id,menu_id):
	return "This page is for editing menu items %s" % menu_id

@app.route("/restaurant/<int:place_id>/menu/<int:menu_id>/delete")
def delete_menu_items(place_id,menu_id):
	return "This page is for deleting menu item %s" % menu_id

@app.route("/api/")
def api():
	return "this is api page"