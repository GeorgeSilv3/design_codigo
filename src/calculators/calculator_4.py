from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from flask import request as FlaskRequest
from typing import Dict, List


class Calculator4:
    def __init__(self, driver_hundler: DriverHandlerInterface) -> None:
        self.__driver_hundler = driver_hundler

    def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
        body = request.json
        input_data = self.__validate_body(body)
        mean = self.__arithmetic_mean(numbers=input_data)
        response = self.__formated_response(mean=mean)
        return response

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("Poorly Body Formated")

        input_data = body["numbers"]
        return input_data
    
    def __arithmetic_mean(self, numbers: List[float]) -> float:
        result = float(self.__driver_hundler.mean(numbers=numbers))
        return result

    def __formated_response(self, mean: float) -> Dict:
        return {
            "data": {
                "Calculator": 4,
                "Value": mean,
                "Success": True
            }
        }