#!/usr/bin/python3
""" """
import os
from sqlalchemy import Column

from tests.test_models.test_base_model import TestBasemodel
from models.user import User


class TestUser(TestBasemodel):
    """ Class representation of test case doe User model"""

    def __init__(self, *args, **kwargs):
        """ Initializes the user class model"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """Test the type of name """
        new = self.value()
        self.assertEqual(
                type(new.first_name),
                str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_last_name(self):
        """Tests type of last_name """
        new = self.value()
        self.assertEqual(
                type(new.last_name),
                str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_email(self):
        """Tests the type of email """
        new = self.value()
        self.assertEqual(
                type(new.email),
                str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_password(self):
        """Tests the type of password """
        new = self.value()
        self.assertEqual(
                type(new.password),
                str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )
