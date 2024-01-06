from flask import Blueprint, jsonify, request, abort, Response, session, redirect, url_for, make_response

model = Blueprint('model', __name__)

@model.route("/setup", methods=["GET"])
def setup():
    if request.method == "GET":
        