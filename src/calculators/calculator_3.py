from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError
from src.errors.http_bad_request import HttpBadRequestError
from flask import request as FlaskRequest
from typing import Dict, List

'''
N numeros sao colocados como entrada

caso a varianca de todos esses numeros for menor que a multiplicacao deles, eh apresentado uma informacao de sucesso ao usuario

caso contrario, eh apresentado uma infromacao de falha
- paa o calculo de variancia, utilize o metodo var da lib numpy
'''

class Calculator3:
    def __init__(self, driver_hundle: DriverHandlerInterface) -> None:
        self.__driver_hundle = driver_hundle

    def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
        body = request.json
        input_data = self.__validate_body(body=body)

        variance = self.__calculate_variance(numbers=input_data)
        multiplication = self.__calculate_multiplication(numbers=input_data)

        self.__verify_result(variance=variance, multiplication=multiplication)

        response = self.__formated_response(variance)
        return response

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("Poorly formated body")

        input_data = body["numbers"]
        return input_data
    
    def __calculate_variance(self, numbers: List[float]) -> float:
        variance = float(self.__driver_hundle.variance(numbers))
        return variance
    
    def __calculate_multiplication(self, numbers: List[float]) -> float:
        multiplication = 1
        for num in numbers: multiplication *= num
        
        return multiplication
    
    def __verify_result(self, variance: float, multiplication: float) -> None:
        if variance > multiplication:
            raise HttpBadRequestError("Variance is bigger than multiplication")

    def __formated_response(self, variance) -> Dict:
        return {
            "data": {
                "Calculator": 3,
                "Value": variance,
                "Success": True
            }
        }