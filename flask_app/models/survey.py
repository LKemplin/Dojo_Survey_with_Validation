from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Survey:
    db = "dojo_survey_schema"
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.location = data["location"]
        self.language = data["language"]
        self.comment = data["comment"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @staticmethod
    def validate_survey(survey_data):
        is_valid = True
        if len(survey_data["name"]) == 0:
            flash("Name must not be blank")
            is_valid = False
        if len(survey_data["comment"]) == 0:
            flash("Comment must not be blank")
            is_valid = False
        return is_valid

    @classmethod
    def create_survey(cls, data):
        query = "INSERT INTO dojos (name, location, language, comment, created_at, updated_at) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s, NOW(), NOW())"
        results = connectToMySQL(cls.db).query_db(query, data)
        return results

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        return cls(results[0])