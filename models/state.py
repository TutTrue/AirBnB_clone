#!usr/bin/python3

""" State model """
from models.base_model import BaseModel


class State(BaseModel):
    """ State class """
    name = ""

    def __init__(self, *args, **kwargs):
        """init the state class"""
        super().__init__(*args, **kwargs)
