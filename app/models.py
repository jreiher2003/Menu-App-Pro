import datetime # pragma: no cover
from app import db # pragma: no cover
from slugify import slugify # pragma: no cover
from flask.ext.security import UserMixin, RoleMixin
from flask.ext.security.utils import encrypt_password


# Define models
roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

    # def __init__(self, username, email, password):
    #     self.username = username
    #     self.email = email 
    #     self.password = encrypt_password(password)

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


    @property 
    def serialize(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "address" : self.address,
            "city" : self.city,
            "state" : self.state,
            "zip_" : self.zip_,
            "website" : self.website,
            "phone" : self.phone,
            "owner" : self.owner,
            "yrs_open" : self.yrs_open
        } 

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

    @property 
    def serialize(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "course" : self.course,
            "description" : self.description,
            "price" : self.price
        } 

    def __repr__(self):
        return '<MenuItem %r>' % (self.name)