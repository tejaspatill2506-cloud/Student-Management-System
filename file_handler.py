import json
import os

FILE_NAME = "students.json"


def load_students():

    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)
            return data
    except:
        return []


def save_students(student_list):

    with open(FILE_NAME, "w") as file:
        json.dump(student_list, file, indent=4)