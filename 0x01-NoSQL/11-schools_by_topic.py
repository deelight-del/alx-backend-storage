#!/usr/bin/env python3
"""This module contains python code that
filters a document based on the given topic using PyMongo"""


def schools_by_topic(mongo_collection, topic):
    """Function implementation to check if a given
    topic is present in a given collection"""
    return [
        d for d in
        mongo_collection.find({"topics": {"$in": [topic]}})
    ]
