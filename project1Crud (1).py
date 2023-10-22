#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 03:17:53 2023

@author: noyaljacob_snhu
"""
import pymongo

class Project1Database:
    def __init__(self, username, password):
        # Customizing the connection variables for your MongoDB environment
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31387
        DB = 'AAC'
        COL = 'animals'

        # Initializing the MongoClient with the customized variables
        self.client = pymongo.MongoClient(f'mongodb://{username}:{password}@{HOST}:{PORT}')
        self.database = self.client[DB]
        self.collection = self.database[COL]

    def create_document(self, data):
        try:
            result = self.collection.insert_one(data)
            return True if result.inserted_id else False
        except Exception as e:
            print(f"Error during insert: {e}")
            return False

    def read_documents(self, query):
        try:
            cursor = self.collection.find(query)
            result = list(cursor)
            return result
        except Exception as e:
            print(f"Error during query: {e}")
            return []

    def update_document(self, query, new_data):
        try:
            result = self.collection.update_many(query, {"$set": new_data})
            return result.modified_count
        except Exception as e:
            print(f"Error during update: {e}")
            return 0

    def delete_documents(self, query):
        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except Exception as e:
            print(f"Error during delete: {e}")
            return 0

    def query_mongodb(self, query):
        try:
            cursor = self.collection.find(query)
            result = list(cursor)
            return result
        except Exception as e:
            print(f"Error during query: {e}")
            return []
        
    def read(self, query):
        try:
            cursor = self.collection.find(query)
            result = list(cursor)
            return result
        except Exception as e:
            print(f"Error during query: {e}")
            return []
