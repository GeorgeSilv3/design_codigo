from src.main.factories.calculator1_factory import calculator1_factory
from src.main.factories.calculator2_factory import calculator2_factory
from src.main.factories.calculator3_factory import calculator3_factory
from src.main.factories.calculator4_factory import calculator4_factory
from src.errors.error_controller import handler_errors
from flask import Blueprint, jsonify, request

calc_route_bp = Blueprint("calc_routes", __name__)

@calc_route_bp.route("/calculator/1", methods=["POST"])
def calculator_1():
    try:
        data = request
        calculator1 = calculator1_factory()
        response = calculator1.calculate(data)
        return jsonify(response)
    except Exception as exception:
        error_response = handler_errors(exception)
        return jsonify(error_response["body"]), error_response["status_code"]


@calc_route_bp.route("/calculator/2", methods=["POST"])
def calculator_2():
    try:
        data = request
        calc = calculator2_factory()
        response = calc.calculate(data)
        return jsonify(response)
    except Exception as exception:
        error_response = handler_errors(exception)
        return jsonify(error_response["body"]), error_response["status_code"]


@calc_route_bp.route("/calculator/3", methods=["POST"])
def calculator_3():
    try:
        data = request
        calc = calculator3_factory()
        response = calc.calculate(data)
        return jsonify(response)
    except Exception as exception:
        error_response = handler_errors(exception)
        return jsonify(error_response["body"]), error_response["status_code"]
    

@calc_route_bp.route("/calculator/4", methods=["POST"])
def calculator_4():
    try:
        data = request
        calc = calculator4_factory()
        response = calc.calculate(data)
        return jsonify(response)
    except Exception as exception:
        error_reponse = handler_errors(exception)
        return jsonify(error_reponse["body"]), error_reponse["status_code"]

@calc_route_bp.route("/teste", methods=["GET"])
def get_calculator():
    return "<h1>Teste Teste</h1>"

