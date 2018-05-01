"""Manually trigger question generation."""

from flask_restful import Resource
from .generate_questions import generate
import json


class GenerateQuestions(Resource):
    """Manually trigger question generation."""

    @staticmethod
    def get(cur):
        """Manually trigger question generation."""
        return json.dumps({"questions": generate(cur)}, indent=4)
