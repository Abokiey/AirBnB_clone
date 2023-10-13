#!/usr/bin/python3
""" Review Class"""
from .base_model import BaseModel

class Review(BaseModel):
    """Blueprint for review"""
    place_id = ""
    user_id = ""
    text = ""