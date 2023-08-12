#!usr/bin/python3

""" Amenity model """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Amenity class """

    name = ""

    def __init__(self, *args, **kwargs):
        """init the Amenity object"""
        super().__init__(*args, **kwargs)
