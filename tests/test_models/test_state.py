#!/usr/bin/python3
""" """
import os

from tests.test_models.test_base_model import TestBasemodel
from models.state import State


class TestState(TestBasemodel):
    """Class definition for State class """

    def __init__(self, *args, **kwargs):
        """ Initializes the class"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """Test case for name3 type """
        new = self.value()
        self.assertEqual(
                type(new.name),
                str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )
