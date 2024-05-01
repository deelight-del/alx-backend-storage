#!/usr/bin/env python3
"""This module contains python code that
that sorts documents by average score"""


from statistics import mean


def top_students(mongo_colleciton):
    """Function implementaion of sorting
    documents"""

    # Initialize an empty list to return when filled.
    return sorted([
        {
            "_id": document.get('_id'),
            "name": document.get('name'),
            "averageScore": mean(
                [topic.get('score')for topic in document.get('topics')]
            )
        }
        for document in mongo_colleciton.find()
    ], key=lambda x: x.get("averageScore"), reverse=True)
