#!/usr/bin/python3
"""
Defines the Review class
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent a Review
       Attributes:
           place_id = empty string
           user_id = empty string
           test = empty string
    """

    place_id = ""
    user_id = ""
    text = ""
