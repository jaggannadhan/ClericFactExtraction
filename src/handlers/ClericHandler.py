from flask import Blueprint, render_template, request, jsonify
from src.services.ClericService import ClericService

cleric = Blueprint("cleric", __name__, url_prefix="/cleric")

@cleric.route("/")
def inputPage():
    return render_template("ClericSubmit.html")

@cleric.route("/submit_question_and_documents", methods=["POST"])
def submit():
    data = request.get_json(force=True)

    serviceClient = ClericService()
    response = serviceClient.manageSubmit(data)

    return jsonify({
        "status_code": 200,
        "response": response
    })

@cleric.route("/push-queue", methods=["POST"])
def process():
    data = request.get_json(force=True)

    serviceClient = ClericService()
    response = serviceClient.processSubmit(data)

    return jsonify(response)

@cleric.route("/get_question_and_facts", methods=["GET"])
def getQuestionAndFacts():
    serviceClient = ClericService()

    response = serviceClient.getQuestionAndFacts()

    return jsonify(response)