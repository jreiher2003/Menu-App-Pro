import unittest 
from base import BaseTestCase 
from flask.ext.login import current_user
from app.models import User
from app import bcrypt

class TestUser(BaseTestCase):

    def test_user_registeration(self):
        with self.client:
            response = self.client.post("/signup", data=dict(
                username="Michael", email="michael@bulls.com",
                password="python", confirm="python", accept_tos="y"
            ), follow_redirects=True)
            self.assertIn(b"Thanks for registering", response.data)
            # self.assertEqual(current_user.is_active())
            # self.assertTrue(current_user.username == "Michael")
            # from pprint import pprint
            # pprint(dir(current_user))
            user = User.query.filter_by(email="michael@bulls.com").first()
            self.assertTrue(user.username) == "Michael"

    def test_get_by_id(self):
        with self.client:
            self.client.post("/login", data=dict(
                email="jeffreiher@gmail.com", password="password"
            ), follow_redirects=True)
            self.assertTrue(current_user.id == 1)
            self.assertFalse(current_user.id == 20)

    def test_check_password(self):
        user = User.query.filter_by(email="jeffreiher@gmail.com").first()
        self.assertTrue(bcrypt.check_password_hash(user.password, "password"))
        self.assertFalse(bcrypt.check_password_hash(user.password, "foobar"))

    
if __name__ == "__main__":
    unittest.main()