#!/usr/bin/python3

"""
class BaseModel that defines all common
methods for other classes
"""

from models.base_model import BaseModel
from uuid import uuid4
from datetime import datetime
import json
import models
import os

class FileStorage:

    __file_path = "file.json"
    __objects = {}
    dict_clases = {"BaseModel": BaseModel}

    def all(self):
        """Public instance

        Returns:
            [self]: [the dictionary objects]
        """
        return self.__objects

    def new(self, obj):
        """[sets in __objects the obj with key <obj class name>.id]

        Args:
            obj ([objects]): [new objets]
        """
        key_compoust = obj.__class__.__name__ + "." + obj.id
        # en los diccionarios si la clave no existe la crea,
        # y si existe la reemplaza.
        self.__objects[key_compoust] = obj

    def save(self):
        """[serializes __objects to the JSON file]
        """
        dict_string = {}
        for key, value in self.__objects.items():
                dict_string[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='UTF8') as file:
            json.dump(dict_string, file, indent=4)

    def reload(self):
        """[ deserializes the JSON file to __objects]
        """
        from models.base_model import BaseModel
        dict_reload = {}
        try:
            with open(self.__file_path) as file:
                dict_desco = json.load(file)
            for key, value in dict_desco.items():
                self.__objects[key] = FileStorage.dict_clases[value["__class__"]](**value)
        except:
            return