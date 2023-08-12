#!usr/bin/python3

""" Base model """
import datetime
import uuid
import models 

class BaseModel():
    """ BaseModel class """
    
    def __init__(self, *args, **kwargs):

        if not kwargs:
            self.id= str(uuid.uuid4())
            self.created_at=datetime.datetime.now()
            self.updated_at=datetime.datetime.now()
            models.storage.new(self)

        else:
            for key, val in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        setattr(self, key,datetime.datetime.fromisoformat(val))
                    else:
                        setattr(self, key, val)
    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
        
            
    def save(self):
        self.updated_at = datetime.datetime.now()
        models.storage.save()
        
    def to_dict(self):
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        
        return my_dict
        
        
        
