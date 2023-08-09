#!/usr/bin/python3
from sys import path
path.append('../AirBnB_clone')
from models.base_model import BaseModel
from models.user import User


my_model = User()
my_model.first_name = "Betty"
my_model.last_name = "Bar"
my_model.email = "airbnb@mail.com"
my_model.password = "root"
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

print("--")
my_new_model = User(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))
print("--------------")
print(my_new_model.to_dict())
my_new_model.save()
print("--")
print(my_model is my_new_model)
