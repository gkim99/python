from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)
import re
LETTERS_ONLY_REGEX = re.compile(r'^[a-zA-Z]+$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL('recipes').query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('recipes').query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL('recipes').query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM users where id = %(id)s;"
        results = connectToMySQL('recipes').query_db(query, data)
        if not results or len(results) == 0:
            return False
        else:
            return cls(results[0])

    @staticmethod
    def validate_register(user):
        is_valid = True

        if len(user['first_name']) == 0:
            flash("First name is a required field", "first_name")
            is_valid = False
        elif len(user['first_name']) < 2:
            flash("First name must be at least 2 characters", "first_name")
            is_valid = False
        elif not LETTERS_ONLY_REGEX.match(user['first_name']):
            flash("First name must only contain alphabetic characters", "first_name")
            is_valid = False

        if len(user['last_name']) == 0:
            flash("Last name is a required field", "last_name")
            is_valid = False
        elif len(user['last_name']) < 2:
            flash("Last name must be at least 2 characters", "last_name")
            is_valid = False
        elif not LETTERS_ONLY_REGEX.match(user['last_name']):
            flash("Last name must only contain alphabetic characters", "last_name")
            is_valid = False

        if len(user['email']) == 0:
            flash("Email is a required field", "email")
            is_valid = False
        elif not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!", "email")
            is_valid = False
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL('recipes').query_db(query, user)
        if len(results) >= 1:
            flash("Email already taken.", "email")
            is_valid=False

        if len(user['password']) == 0:
            flash("Password is a required field", "password")
            is_valid = False
        elif len(user['password']) < 8:
            flash("Password must be at least 8 characters", "password")
            is_valid = False
        elif user['password'] != user['cpassword']:
            flash("Password and Confirm Password does not match", "password")
            is_valid = False
        return is_valid

    @staticmethod
    def validate_login(user_login):
        user = User.get_by_email(user_login)
        if not user:
            flash("Invalid email/password", "login")
            return False
        elif not bcrypt.check_password_hash(user.password, user_login['password']):
            flash("Invalid email/password", "login")
            return False
        return user