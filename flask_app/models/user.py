from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data): 
        query = """INSERT INTO users(first_name, last_name, email, password, created_at,updated_at) 
                VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, Now(),Now());"""
        return connectToMySQL('user-test').query_db(query, data) 

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('user-test').query_db(query)
        # convert list of dictionaries into a list of class instances
        users = []
        for user in results:
            users.append(cls(user))

        return users
    
    @classmethod
    def get_one_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s"
        result = connectToMySQL('user-test').query_db(query,data)
        # if user with this email doesn't exist, return false
        if len(result) < 1:
            return False
        # create class instance of user returned
        return cls(result[0])
    
    @staticmethod
    def validate_registration(user):
        is_valid = True
        if len(user['first_name']) < 2:
            flash("First Name must be at least 3 characters.")
            is_valid = False
        if len(user['last_name']) < 2:
            flash("Last Name must be at least 3 characters.")
            is_valid = False
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters.")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid Email!!!","register")
            is_valid = False
        if user['password'] != user['confirm_pw']:
            flash('Password and Confirm Password do not match!')
            is_valid = False
        return is_valid

    
    # @staticmethod
    # def validate_login(user):






