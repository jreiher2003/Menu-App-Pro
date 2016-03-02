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