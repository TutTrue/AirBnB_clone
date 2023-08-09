#!usr/bin/python3

""" User model """
from models.base_model import BaseModel
import datetime
import uuid
import models 

class User(BaseModel):
    """ User class """
    
    email=""
    password =""
    first_name =""
    last_name = ""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
