from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError
from typing import Dict, List
from flask import request as FlaskRequest

class Calculator2:
    def __init__(self, driver_hundle: DriverHandlerInterface) -> None:
        self.__driver_hundler = driver_hundle

    def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
        body = request.json
        input_data = self.__validate_body(body)
        calc_result = self.__process_data(input_data=input_data)
        formated_response = self.__format_response(calc_result=calc_result)

        return formated_response
    

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("Poorly formated body")
        
        input_data = body["numbers"]
        return input_data
    

    def __process_data(self, input_data: List[float]) -> float:
        first_process_result = [(x * 11) ** 0.95 for x in input_data]
        result = float(self.__driver_hundler.standard_derivation(numbers=first_process_result))

        return 1/result
    

    def __format_response(self, calc_result: float) -> Dict:
        return {
            "data": {
                "calculator": 2,
                "result": round(calc_result, 2)
            }
        }