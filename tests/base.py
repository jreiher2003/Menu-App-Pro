import datetime
from flask.ext.testing import TestCase
from app import app, db
from app.models import Place, Menu, User






class BaseTestCase(TestCase):
    """A base test case."""
 
    def create_app(self):
        app.config.from_object('config.TestConfig')
        # from app.users.views import users_blueprint
        # from app.api.views import api_blueprint
        # from app.home.views import home_blueprint
        # app.register_blueprint(users_blueprint) 
        # app.register_blueprint(api_blueprint)
        # app.register_blueprint(home_blueprint)
        return app

    def setUp(self):
        db.create_all()
        db.session.add(Place(name='Testname',
                             address="123 Test st.",
                             city="Englewood",
                             state="Florida",
                             zip_="34224",
                             website="http://fake.com",
                             phone="123-456-7899",
                             owner="Jeff Reiher",
                             yrs_open=1))

        db.session.add(Menu(name="burger",
                            course="dinner",
                            description="test description",
                            price="$1.00"))
        
        db.session.add(User(username="Jeffrey",
                            email="jeffreiher@gmail.com",
                            password="password",
                            avatar="picofjeff.jpg"))

        
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
