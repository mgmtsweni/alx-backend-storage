#!/usr/bin/env python3
"""MongoDB with Python"""


def schools_by_topic(mongo_collection, topic):
    """function that returns the list of school"""
    my_filter = {
        'topics': {
            '$elemMatch': {
                '$eq': topic,
            },
        },
    }
    return list(mongo_collection.find(my_filter))
