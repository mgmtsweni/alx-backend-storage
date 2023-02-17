#!/usr/bin/env python3
"""MongoDB with Python"""


def list_all(mongo_collection):
    """function that lists all documents"""
    return list(mongo_collection.find()) if mongo_collection else []
