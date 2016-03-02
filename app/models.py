import datetime # pragma: no cover
from app import db # pragma: no cover
from slugify import slugify # pragma: no cover

class Place(db.Model):

    __tablename__ = 'place' 

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(250))
    city = db.Column(db.String(80))
    state = db.Column(db.String(20))
    zip_ = db.Column(db.String(10))
    website = db.Column(db.String)
    phone = db.Column(db.String)
    owner = db.Column(db.String)
    yrs_open = db.Column(db.Integer)


    def __init__(self, name, address, city, state, zip_, website, phone, owner, yrs_open):
    	self.name = name
    	self.address = address
    	self.city = city
    	self.state = state
    	self.zip_ = zip_
    	self.website = website
    	self.phone = phone 
    	self.owner = owner
    	self.yrs_open = yrs_open

    @property 
    def name_slug(self):
        return slugify(self.name)

    def __repr__(self):
        return '<Place %r>' % (self.name)


class Menu(db.Model):
    __tablename__ = 'menu'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    course = db.Column(db.String(250))
    description = db.Column(db.String(250))
    price = db.Column(db.String(8))
    place_id = db.Column(db.Integer, db.ForeignKey('place.id'))
    place = db.relationship(Place)

    @property 
    def name_slug(self):
        return slugify(self.name)

    def __repr__(self):
        return '<MenuItem %r>' % (self.name)