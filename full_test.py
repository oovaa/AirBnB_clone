#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.review import Review
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity

# Reload objects from the storage
all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

# Create a new Review
print("-- Create a new Review --")
my_review = Review()
my_review.text = "Great experience!"
my_review.save()
print(my_review)

# Create a new Place
print("-- Create a new Place --")
my_place = Place()
my_place.name = "Cozy Cabin"
my_place.price_per_night = 100
my_place.save()
print(my_place)

# Create a new State
print("-- Create a new State --")
my_state = State()
my_state.name = "California"
my_state.save()
print(my_state)

# Create a new City
print("-- Create a new City --")
my_city = City()
my_city.name = "San Francisco"
my_city.state_id = my_state.id
my_city.save()
print(my_city)

# Create a new Amenity
print("-- Create a new Amenity --")
my_amenity = Amenity()
my_amenity.name = "Wi-Fi"
my_amenity.save()
print(my_amenity)
