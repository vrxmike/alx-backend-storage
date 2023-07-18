#!/usr/bin/env python3
"""
students
"""


def top_students(mongo_collection):
    """ students by score """
    return mongo_collection.aggregate([
        {
            "$project":
                {
                    "name": "$name",
                    "averageScore": {"$avg": "$topics.scoere"}
                }
        },
        {
            "$sort":
                {
                    "averageScore": -1
                }
        }
    ])
