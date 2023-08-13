#!/usr/bin/python3
"""Unittest for Place model
"""
import unittest
from models.place import Place


class Test_Place_model(unittest.TestCase):
    """
    test class for the Place model.
    """
    def test_default_values(self):
        """test default values for Place model"""

        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])
