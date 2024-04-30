#!/usr/bin/env python3
"""This module contains python code that
updates a document based on the given name using PyMongo"""


def update_topics(mongo_collection, name, topics):
    """Function implementatin of updating a given document
    based on the name"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
