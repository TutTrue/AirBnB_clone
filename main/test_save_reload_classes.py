#!/usr/bin/python3
from sys import path
path.append('../AirBnB_clone')
from models import storage
from models.base_model import BaseModel
from models.place import Place
from models.state import State 
from models.city import City 
from models.amenity import Amenity 
from models.review import Review 

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new Place --")
my_place = Place()
my_place.description = "new place"
my_place.name = "Bar"


my_place.save()
print(my_place)

print("-- Create a new Place 2 --")
my_place2 = Place()
my_place2.save()
print(my_place2)


print("-- Create a new City")

my_city = City()
my_city.save()
print(my_city)

print("-- Create a new Review")
my_review = Review()
my_review.save()
print(my_review)


print("-- Create a new Amenity")

my_amenity = Amenity()
my_amenity.save()
print(my_amenity)


print("-- Create a new State")

my_state = State()
my_state.save()
print(my_state)
