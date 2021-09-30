from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app
from flask_app.models import user

class Recipe:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.under_30_mins = data['under_30_mins']
        self.instructions = data['instructions']
        self.date_made_on = data['date_made_on']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL('recipes').query_db(query)

        recipes = []
        for recipe in results:
            recipes.append(cls(recipe))
        return recipes

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM recipes LEFT JOIN users ON recipes.user_id = users.id WHERE recipes.id = %(id)s;"
        results =  connectToMySQL('recipes').query_db(query, data)
        return cls(results[0])

    @classmethod
    def update_one(cls, data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instruction)s, date_made_on = %(date_made_on)s, under_30_mins = %(under_30_mins)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('recipes').query_db(query, data)

    @classmethod
    def save(cls, data):
        query = "INSERT INTO recipes (name, description, under_30_mins, instructions, date_made_on, user_id, created_at, updated_at) VALUES (%(name)s, %(description)s, %(under_30_mins)s, %(instructions)s, %(date_made_on)s, %(user_id)s, NOW(), NOW());"
        return connectToMySQL('recipes').query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL('recipes').query_db(query, data)
    
    @staticmethod
    def validate_recipe(recipe):
        is_valid = True
        if not recipe['name']:
            flash("Name is a required field", "name")
            is_valid = False
        elif len(recipe['name']) < 3:
            flash("Name must be at least 3 characters", "name")
            is_valid = False

        if not recipe['description']:
            flash("Description is a required field", "description")
            is_valid = False
        elif len(recipe['description']) < 3:
            flash("Description must be at least 3 characters", "description")
            is_valid = False

        if not recipe['instructions']:
            flash("Instructions is a required field", "instructions")
            is_valid = False
        elif len(recipe['instructions']) < 3:
            flash("Instructions must be at least 3 characters", "instructions")
            is_valid = False

        return is_valid