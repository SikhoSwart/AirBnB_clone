#!/usr/bin/python3
"""Class user. for AirBnB"""
from models.base_model import BaseModel


class User(BaseModel):
    """Clas user, inherits from basemodel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
