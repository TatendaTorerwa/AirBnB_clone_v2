#!/usr/bin/python3
""" Test module for Place model"""

import os


from tests.test_models.test_base_model import TestBasemodel
from models.place import Place


class test_Place(TestBasemodel):
    """Represents tests for place model """

    def __init__(self, *args, **kwargs):
        """Initializes the test class """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """Tets type of city_id """
        new = self.value()
        self.assertEqual(
                type(new.city_id),
                str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_user_id(self):
        """ Tests type of user_id"""
        new = self.value()
        self.assertEqual(
                type(new.user_id),
                str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_name(self):
        """Test the name """
        new = self.value()
        self.assertEqual(
                type(new.name),
                str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_description(self):
        """Tests thetype of description """
        new = self.value()
        self.assertEqual(
                type(new.description),
                str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_number_rooms(self):
        """ Tests for number of rooms"""
        new = self.value()
        self.assertEqual(
                type(new.number_rooms),
                int if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_number_bathrooms(self):
        """Test the number of bathrooms """
        new = self.value()
        self.assertEqual(
                type(new.number_bathrooms),
                int if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_max_guest(self):
        """Test for number of guest """
        new = self.value()
        self.assertEqual(
                type(new.max_guest),
                int if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_price_by_night(self):
        """Tests for price by night """
        new = self.value()
        self.assertEqual(
                type(new.price_by_night),
                int if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_latitude(self):
        """Tests for latitude """
        new = self.value()
        self.assertEqual(
                type(new.latitude),
                float if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_longitude(self):
        """Tests for longitude """
        new = self.value()
        self.assertEqual(
                type(new.latitude),
                float if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_amenity_ids(self):
        """Tests the type of amenity_ids"""
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
