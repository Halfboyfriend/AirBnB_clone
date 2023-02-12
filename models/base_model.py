#!/usr/bin/python3
"""
Custom base class for all project work.
"""

import uuid
from datetime import datetime
import models


class BaseModel():
    """
    BASEMODEL CLASS

     Attributes:
        id(str): handles unique user identity
        created_at: assigns current datetime
        updated_at: updates current datetime
    Methods:
        __str__: prints the class name, id, and creates dictionary
        representations of the input values
        save(self): updates instance attributes with current datetime
        to_dict(self): returns the dictionary values of the instance obj
    """

    def __init__(self, *args, **kwargs):

        DATE_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)


        else:
            for key, value in kwargs:
                if key in ("updated_at", "created_at"):
                    self.__dict__[key] = datetime.strptime(value, DATE_FORMAT)
                elif key[0] == "id":
                    self.__dict__[key] = str(value)
                else:
                    self.__dict__[key] = value

    def __str__(self):
        """
        return: Strings rep of class
        """
        return f"[{self.__class__.__name__} ({self.id}) {self.__dict__}]"

    def save(self):
        """
        return: update the public instance 'updated_time' with the current date
        time.
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()



    def to_dict(self):
        """
        return: a dictionary containing all key/value pairs
        """
        all_dict = {}

        for k,v in self.__dict__.items():
            if k == "created_at" or k == "updated_at":
                all_dict[k] = v

            else:
                all_dict[k] = v
        return all_dict



