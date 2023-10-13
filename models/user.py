#!/usr/bin/python3
"""
User Class module
"""
from models.base_model import BaseModel

class User(BaseModel):
    """
    User class that inherits from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    