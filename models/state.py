#!/usr/bin/python3
"""This is the State Model module.
The State class that inherits from BaseModel.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """This class will define a State.
        name (str): the state's name.
    """

    name = ""
