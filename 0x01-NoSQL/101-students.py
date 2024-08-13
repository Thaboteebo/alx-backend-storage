#!/usr/bin/env python3
from pymongo import MongoClient


def top_students(mongo_collection):
    """ Returns all students sorted by average score."""
    students = list(mongo_coolection.find())

    for student in students:
        topics = student.get('topics', [])
        if topics:
            total_score = sum(topic['score'] for topic in topics)
            average_score = total_score / len(topics)
        else:
            average_score = 0

        student['averageScore'] = average_score

    student.sort(key=lambda x: x['averageScore'], reverse=True)

    return students


if __name__ = "__main__":
    client = MongoClient('')
    students_collection = client.my_db.students

    top_students_list = top_students(students_collection)
    for student in top_students_list:
        print("[{}] {} => {}".format(student.get('_id'), student.get('name'), student.get('averageScore')))
