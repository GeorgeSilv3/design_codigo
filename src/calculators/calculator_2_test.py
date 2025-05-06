from .calculator_2 import Calculator2
from src.drivers.numpy_handler import NumpyHandler
from typing import Dict

class MocketRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

def test_calculate():
    driver = NumpyHandler()
    calculator_2 = Calculator2(driver_hundle=driver)
    mock_request = MocketRequest({"numbers": [1, 2, 3, 4]})
    response = calculator_2.calculate(mock_request.json)

    print(response)

    assert "data" in response
    assert "calculator" in response["data"]
    assert "result" in response["data"]