#!usr/bin/python3

""" Base model """
import datetime
import uuid
import models


class BaseModel():
    """ BaseModel class """

    def __init__(self, *args, **kwargs):
        """
        init the BaseModel class
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

        else:
            for k, v in kwargs.items():
                if k != "__class__":
                    if k == "created_at" or k == "updated_at":
                        setattr(self, k, datetime.datetime.fromisoformat(v))
                    else:
                        setattr(self, k, v)

    def __str__(self):
        """string representaion for the class"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """save the obj to the json file"""
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """convert the obj to a dict"""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()

        return my_dict
