import sqlite3
from sqlite3.dbapi2 import Connection, Cursor, connect
from flask_restful import Resource
from flask import request

class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password
    
    @classmethod
    def find_by_username(cls, username):
        Connection = sqlite3.Connection('data.db')
        cursor = Connection.cursor()

        query = "SELECT * FROM users WHERE username = ?"
        result = cursor.execute(query, (username,))
        row = result.fetchone()

        if row:
            user = cls(*row)
        else:
            user = None
 
        Connection.close()
        return user

       
    @classmethod
    def find_by_id(cls, _id):
        Connection = sqlite3.Connection('data.db')
        cursor = Connection.cursor()
        query = "SELECT * FROM users WHERE id = ?"
        result = cursor.execute(query, (_id,))
        row = result.fetchone()

        if row:
            user = cls(*row)
        else:
            user = None
 
        Connection.close()
        return user

class UserRegister(Resource):
    def post (self):
        data = request.get_json(force = True)

        if User.find_by_username(data['username']):
            return {'message': 'Es Saxeli Ukve Gamoyenebulia'}

        Connection = sqlite3.Connection('data.db')
        Cursor = Connection.cursor()

        query = "INSERT INTO users VALUES (NULL, ?, ?)"

        Cursor.execute(query, (data['username'], data['password']))

        Connection.commit()
        Connection.close()

        return {'Messages': 'Momxmarebeli Sheiqmna'}

        


