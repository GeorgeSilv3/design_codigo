from src.drivers.numpy_handler import NumpyHandler
from .calculator_3 import Calculator3
from typing import Dict, List
from pytest import raises

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

class MockDriverHandle():
    def variance(self, numbers: List[float]) -> float:
        return 0.24

class MockDriverHundleError():
    def variance(self, numbers: List[float]) -> float:
        return 100000

def test_calculate():
    mock_request = MockRequest({"numbers": [1, 2, 2, 1, 2]})
    calculator_3 = Calculator3(MockDriverHandle())

    response = calculator_3.calculate(mock_request)
    
    assert response == {'data': {'Calculator': 3, 'Value': 0.24, 'Success': True}}

def test_calculate_with_variance_error():
    mock_request = MockRequest({"numbers": [1, 1, 1, 1, 100]})
    calculator_3 = Calculator3(MockDriverHundleError())

    with raises(Exception) as excinfo:
        calculator_3.calculate(mock_request)

        assert excinfo.value == "Poorly formated body"
