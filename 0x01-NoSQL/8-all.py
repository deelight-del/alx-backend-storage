#!/usr/bin/env python3
"""This module contains python code that
lists all documents in a collection"""


def list_all(mongo_collection):
    """Implementation of the list all function"""
    return [d for d in mongo_collection.find()]
