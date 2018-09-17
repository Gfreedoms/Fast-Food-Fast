from flask import jsonify


class FeedbackResponse:
    @staticmethod
    def display(message, code):
        return jsonify({"message": message}), code
