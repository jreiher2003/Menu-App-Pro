from app import app,db # pragma: no cover
from app.models import Place, Menu # pragma: no cover
from flask import render_template, request, url_for, redirect, flash, jsonify # pragma: no cover
import us # pragma: no cover 

@app.route("/") 
@app.route("/restaurant/")
def show_places(): 
    all_places = Place.query.all()
    return render_template(
        'restaurants.html', 
        all_places=all_places)

@app.route("/restaurant/new", methods=["GET", "POST"])
def new_place():
    states = us.states.STATES 
    if request.method == "POST":
        new = Place(
            name=request.form["name"],
            address=request.form["address"],
            city=request.form["city"],
            state=request.form["state"],
            zip_=request.form["zip_"],
            website=request.form["website"],
            phone=request.form["phone"],
            owner=request.form["owner"],
            yrs_open=request.form["yrs_open"]
            )
        db.session.add(new)
        db.session.commit()
        flash("You just added a new restaurant", "success")
        return redirect(url_for("show_places"))
    return render_template("new_restaurant.html", states=states)

@app.route("/restaurant/<int:place_id>/edit", methods=["GET", "POST"])
def edit_place(place_id):
    edit_rest = Place.query.filter_by(id=place_id).one()
    if request.method == "POST":
        edit_rest.name = request.form["name"]
        edit_rest.address = request.form["address"]
        edit_rest.city = request.form["city"]
        edit_rest.state = request.form["state"]
        edit_rest.zip_ = request.form["zip_"]
        edit_rest.website = request.form["website"]
        edit_rest.phone = request.form["phone"]
        edit_rest.owner = request.form["owner"]
        edit_rest.yrs_open = request.form["yrs_open"]
        db.session.add(edit_rest)
        db.session.commit()
        flash("You just edited this restaurant", "success")
        return redirect(url_for("show_places"))
    return render_template(
        "edit_restaurant.html", 
        place_id=place_id, 
        edit_rest=edit_rest
        ) 

@app.route("/restaurant/<int:place_id>/delete", methods=["GET", "POST"])
def delete_place(place_id):
    delete_rest = Place.query.filter_by(id=place_id).one()
    if request.method == "POST":
        db.session.delete(delete_rest)
        db.session.commit()
        flash("You just deleted %s" % delete_rest.name, "danger")
        return redirect(url_for("show_places"))
    return render_template(
        "delete_restaurant.html", 
        place_id=place_id, 
        delete_rest=delete_rest
        )
    
@app.route("/restaurant/<int:place_id>/menu")
@app.route("/restaurant/<int:place_id>")
def show_menu(place_id):
    place = Place.query.filter_by(id = place_id).one()
    menuitems = Menu.query.filter(Menu.place_id == place_id).all()
    return render_template(
        "menu.html", 
        place=place,
        menuitems=menuitems
        )

@app.route("/restaurant/<int:place_id>/menu/new", methods=["GET", "POST"])
def new_menu_item(place_id):
    if request.method == "POST":
        new_menu = Menu(
            name = request.form["name"],
            course = request.form["course"],
            description = request.form["description"],
            price = request.form["price"],
            place_id = place_id
            )
        db.session.add(new_menu)
        db.session.commit()
        flash("Just add a new menu item", "success")
        return redirect(url_for("show_menu", place_id=place_id))
    return render_template(
        "new_menu.html", 
        place_id=place_id)

@app.route("/restaurant/<int:place_id>/menu/<int:menu_id>/edit", methods=["GET","POST"])
def edit_menu_item(place_id,menu_id):
    edit_menu = Menu.query.filter_by(id=menu_id).one()
    if request.method == "POST":
        edit_menu.name = request.form["name"]
        edit_menu.course = request.form["course"]
        edit_menu.description = request.form["description"]
        edit_menu.price = request.form["price"]
        db.session.add(edit_menu)
        db.session.commit()
        flash("Just edited menu item")
        return redirect(url_for("show_menu", place_id=place_id))
    return render_template("edit_menu.html", 
        place_id=place_id, 
        menu_id=menu_id,
        edit_menu=edit_menu
        )

@app.route("/restaurant/<int:place_id>/menu/<int:menu_id>/delete", methods=["GET","POST"])
def delete_menu_item(place_id,menu_id):
    delete_menu = Menu.query.filter_by(id=menu_id).one()
    if request.method == "POST":
        db.session.delete(delete_menu)
        db.session.commit()
        flash("You just deleted %s" % delete_menu.name, "danger")
        return redirect(url_for("show_menu", place_id=place_id))
    return render_template(
        "delete_menu.html", 
        place_id=place_id, 
        menu_id=menu_id,
        delete_menu=delete_menu
        )

@app.route("/api/")
def api():
    return "this is api page"

@app.route("/restaurant/JSON/")
def restaurant_json():
    places = Place.query.all()
    return jsonify(Restaurants=[i.serialize for i in places])

@app.route("/restaurant/<int:place_id>/menu/JSON")
def menu_json(place_id):
    menu = Menu.query.filter_by(place_id=place_id).all()
    return jsonify(MenuItems=[i.serialize for i in menu])

@app.route("/restaurant/<int:place_id>/menu/<int:menu_id>/JSON")
def single_menu_item(place_id, menu_id):
    menu = Menu.query.filter_by(id=menu_id).all()
    return jsonify(MenuItem=[i.serialize for i in menu])


################################################################
###  Google + login ############################################
################################################################
from flask import session as login_session 
from flask import make_response
import random
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
import requests
from pprint import pprint

CLIENT_ID = json.loads(open("client_secrets.json", "r").read())["web"]["client_id"]
# print CLIENT_ID

@app.route("/login")
def show_login():
    state = "".join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))
    login_session["state"] = state 
    # return " the current session state is %s" % login_session["state"]
    return render_template("login.html", STATE=login_session["state"])

@app.route("/gconnect", methods=["POST"])
def google_signin():
    print request.args.get("state")
    print login_session["state"]
    if request.args.get("state") != login_session["state"]:
        response = make_response(json.dumps("Invalid Credentials"), 401)
        response.headers["Content-Type"] = "application/json"
        return response
    code = request.data
    try:
        oauth_flow = flow_from_clientsecrets("client_secrets.json", scope="")
        pprint(type(oauth_flow))
        # print oauth_flow.auth_uri
        # print oauth_flow.authorization_header
        # print oauth_flow.device_uri
        # print oauth_flow.login_hint 
        # print oauth_flow.redirect_uri
        # print oauth_flow.user_agent
        oauth_flow.redirect_uri = "postmessage" 
        credentials = oauth_flow.step2_exchange(code)
        # print credentials.access_token
        # print credentials.client_id
        # print credentials.client_secret

    except FlowExchangeError:
        response = make_response(json.dumps("Failed to upgrade the authorization code."), 401)
        response.headers["Content-Type"] = "application/json" 
        return response  

    access_token = credentials.access_token 
    print access_token
    url = ("https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s" % access_token)
    h = httplib2.Http() 
    result = json.loads(h.request(url, "GET")[1])
    print result

    if result.get("error") is not None:
        response = make_response(json.dumps(result.get("error")), 500)
        response.headers["Content-Type"] = "application/json"
        return response

    gplus_id = credentials.id_token["sub"]
    if result["user_id"] != gplus_id:
        response = make_response(json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers["Content-Type"] = "application/json"
        return response

    stored_credentials = login_session.get("credentials")
    stored_gplus_id = login_session.get("gplus_id")
    if stored_credentials is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps("Current user is already connected."), 200)
        response.headers["Content-Type"] = "application/json" 
        return response

    login_session["credentials"] = credentials.access_token
    login_session["gplus_id"] = gplus_id 

    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()
    print data

    login_session['username'] = data['name']
    login_session["name"] = data["given_name"]
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'], "success")
    print "done!"
    return output


@app.route("/gdisconnect")
def disconnect():
    access_token = login_session["credentials"]
    print access_token
    print login_session["username"]

    if access_token is None:
        response = make_response(json.dumps("Current user not connected"), 401)
        reponse.headers["Content-Type"] = "application/json"
        return response 
   
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    print url
    h = httplib2.Http()
    result = h.request(url, "GET")[0]
    print result

    if result["status"] == 200:
        del login_session["credentials"]
        del login_session["gplus_id"]
        del login_session["username"]
        del login_session["name"]
        del login_session["email"]
        del login_session["picture"] 

        response = make_response(json.dumps("You just disconnected"), 200)
        response.header["Content-Type"] = "application/json"
        return response 

    else:
        response = make_response(json.dumps("Failed to revoke token for given user."), 400)
        response.headers["Content-Type"] = "application/json"
        return response 



@app.route("/g_login_status/")
def show_me():
    return "yo <img src='%s'><br>%s<br>%s" % (login_session["picture"], login_session["username"], login_session["email"])