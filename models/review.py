#!/usr/bin/python3
""" Review Model Module
It Inherits from BaseModel
"""
from models.base_model import BaseModel


class review(BaseModel):
    """ This class will describe the review
        place_id (str): the review's place id.
        user_id (str): the review's issuer user id.
        text (str): the review.
"""
place_id = ""
user_id = ""
text = ""
