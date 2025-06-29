from pymongo import MongoClient
from bson.objectid import ObjectId

#added this to work with Module 5
import urllib.parse

class AnimalShelter(object):
    """CRUD operations for Animal collection in MongoDB"""

    def __init__(self, user, password):
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 33818
        DB = 'AAC'  
        COL = 'animals'

        # Use user-provided credentials instead of hardcoded ones
        user = urllib.parse.quote_plus(user)
        password = urllib.parse.quote_plus(password)


        # Initialize Connection
        self.client = MongoClient(f'mongodb://{user}:{password}@{HOST}:{PORT}/{DB}?authSource={DB}')
        self.database = self.client[DB]
        self.collection = self.database[COL]


    # Create method (Inserts a new document)
    def create(self, data):
        if data is not None:
            self.collection.insert_one(data)
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    # Read method (Retrieves records)
    def read(self, query={}):
        return list(self.collection.find(query))

    #the Update method (adjusting records)
    def update(self, query, new_values):
        if query and new_values:
            update_result = self.collection.update_many(query, {"$set": new_values})
            return update_result.modified_count
        else: 
            raise Exception("Update failed: Missing query or new values")
    
    
    #Delete Method (remove records)
    def delete(self, query):
        if query:
            delete_results = self.collection.delete_many(query)
            return delete_results.deleted_count
        else:
            raise Exception("Delete failed: Query parameter is empty")
    