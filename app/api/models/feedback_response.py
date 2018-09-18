"""
Module to handle response to users
"""
from flask import jsonify

class FeedbackResponse:
    """
    Class to handle response to users
    """
    @staticmethod
    def display(message, code):
        """
        Display feedback to users
        """
        return jsonify({"Feedback": message}), code
