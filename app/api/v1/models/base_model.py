import json
from datetime import datetime
meetups = []
questions = []
users = []


class BaseModel:
    @staticmethod
    def check_db(db):
        if db == "meetups":
            data_store = meetups
            return data_store
        elif db == "questions":
            data_store = questions
            return data_store
        elif db == "users":
            data_store = users
            return data_store

    def save_data(self, db, data):
        data_store = BaseModel.check_db(db)
        if data_store is questions:
            data["id"] = len(data_store) + 1
            data["votes"] = 0
        elif data_store is meetups:
            data["id"] = len(data_store) + 1
            data["createdOn"] = json.dumps(datetime.now(), default=str)
        elif data_store is users:
            data["id"] == len(data_store) + 1
            data["registeredOn"] = json.dumps(datetime.now(), default=str)
        data_store.append(data)
        return data_store

    def retrieve_data(self, db):
        data_store = BaseModel.check_db(db)
        return data_store

    def find_by_id(self, db, id):
        data_store = BaseModel.check_db(db)
        specific_data = [
            stored_data for stored_data in data_store if stored_data["id"] == id]
        if specific_data:
            return specific_data
        return "Record doesn't exist."
