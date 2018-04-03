"""Implemenet the assistant."""

from flask_restful import Resource
from flask import request
import watson_developer_cloud
import os

conversation = watson_developer_cloud.ConversationV1(
    username=os.environ["watson_username"],
    password=os.environ["watson_password"],
    version=os.environ["watson_version"]
)
workspace_id = os.environ["watson_workspace"]


class Assistant(Resource):
    """Implement the assistant."""

    @staticmethod
    def post(cur):
        """Return Watson's response to a query."""
        return conversation.message(workspace_id, input={"text": request.form.get('text')})['output']['text']
