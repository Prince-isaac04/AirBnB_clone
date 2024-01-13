#!/usr/bin/python3
""" User Class
This is the user class that inherits from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """ User class that inherits BaseModel
        email(str) = users' email
        password(str) = users' password
        first_name(str) = users' firstname
        last_name(str) = users' lastname
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
