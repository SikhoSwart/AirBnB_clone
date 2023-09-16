#!/usr/bin/python3
"""Class Review for airbnb"""
from models.base_model import BaseModel


class Review(BaseModel):
    """class review, inherits BaseModel """
    place_id = ""
    user_id = ""
    text = ""
