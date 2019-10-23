from flask import Blueprint, jsonify, request

array = ['dogs', 'cats', 'chickens']

array_api = Blueprint('array_api', __name__)


@array_api.route('/array', methods=['GET'])
def serve_array():
    return jsonify({"animals": array})

@array_api.route('/todo', methods=['POST'])
def add_todo():
    array.append(request.json["item"])
    print(array)
    return jsonify(success=True) 