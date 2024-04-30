#!/usr/bin/env python3
"""This module contains python code that
inserts a document into a collection using PyMongo"""


def insert_school(mongo_collection, **kwargs):
    """Function implementation of insert_school"""
    return mongo_collection.insert_one(kwargs).inserted_id
