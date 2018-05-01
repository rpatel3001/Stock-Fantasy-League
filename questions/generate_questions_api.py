"""Manually trigger question generation."""

from flask_restful import Resource
from .generate_questions import generate
from flask import jsonify


class GenerateQuestions(Resource):
    """Manually trigger question generation."""

    @staticmethod
    def get(cur):
        """Manually trigger question generation."""
        return jsonify({"questions": generate(cur)})
