from app import app,db # pragma: no cover
from app.models import Place, Menu # pragma: no cover
from flask import render_template # pragma: no cover

@app.route("/") 
@app.route("/restaurants")
def show_places(): 
	all_places = Place.query.all()
	return render_template('restaurants.html', 
		all_places=all_places)

@app.route("/restaurant/new")
def new_place():
	return render_template("new_restaurant.html")

@app.route("/restaurant/<int:place_id>/edit")
def edit_place(place_id):
	return render_template("edit_restaurant.html", place_id=place_id) 

@app.route("/restaurant/<int:place_id>/delete")
def delete_place(place_id):
	return render_template("delete_restaurant.html", place_id=place_id)
	
@app.route("/restaurant/<int:place_id>/menu")
@app.route("/restaurant/<int:place_id>")
def show_menu(place_id):
	place = Place.query.filter_by(id = place_id).one()
	menuitems = Menu.query.filter(Menu.place_id == place_id).all()
	return render_template("menu.html", 
		place=place,
		menuitems=menuitems)

@app.route("/restaurant/<int:place_id>/menu/new")
def new_menu_item(place_id):
	return render_template("new_menu.html", place_id=place_id)

@app.route("/restaurant/<int:place_id>/menu/<int:menu_id>/edit")
def edit_menu_item(place_id,menu_id):
	return render_template("edit_menu.html", place_id=place_id, menu_id=menu_id)

@app.route("/restaurant/<int:place_id>/menu/<int:menu_id>/delete")
def delete_menu_item(place_id,menu_id):
	return render_template("delete_menu.html", place_id=place_id, menu_id=menu_id)

@app.route("/api/")
def api():
	return "this is api page"