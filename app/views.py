from app import app,db # pragma: no cover
from app.models import Place, Menu # pragma: no cover
from flask import render_template # pragma: no cover

@app.route("/") 
def index(): 
	all_places = Place.query.all()
	return render_template('index.html', all_places=all_places)

@app.route("/create-new-restaurant")
def create_new_place():
	return "new create-new-restaurant"

@app.route("/<int:place_id>/<path:place_name>/")
def place_menu(place_id,place_name):
	menuitems = Menu.query.filter(Menu.place_id == place_id).all()
	return render_template("menu.html", menuitems=menuitems)


@app.route("/<int:place_id>/<path:place_name>/edit/")
def place_edit(place_id,place_name):
	return "place edit"

@app.route("/<int:place_id>/<path:place_name>/delete/")
def place_delete(place_id,place_name):
	return "place delete"

@app.route("/create-new-menu-item")
def create_new_menu_item():
	return "create new menu item"

@app.route("/<int:place_id>/<path:place_name>/<int:menu_id>/<path:menu_name>/edit")
def edit_menu_items(place_id,place_name,menu_id,menu_name):
	return "edit menu item"

@app.route("/<int:place_id>/<path:place_name>/<int:menu_id>/<path:menu_name>/delete")
def delete_menu_items(place_id,place_name,menu_id,menu_name):
	return "delete menu item"

@app.route("/api")
def api():
	return "this is api page"