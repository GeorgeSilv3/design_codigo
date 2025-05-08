from .calculator_4 import Calculator4
from typing import Dict, List
from pytest import raises

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

class MockDriverHundle:
    def mean(self, numbers: List[float]) -> float:
        return 3.0

def test_calculator4():
    calc = Calculator4(MockDriverHundle())
    mocked_request = MockRequest({"numbers": [1, 2, 3, 4, 5]})
    response = calc.calculate(request=mocked_request)
    
    assert response == {'data': {'Calculator': 4, 'Value': 3.0, 'Success': True}}

def test_calculator4_error():
    calc = Calculator4(MockDriverHundle())
    mocked_request = MockRequest({"number": [1, 2, 3, 4, 5]})

    with raises(Exception) as excinfo:
        response = calc.calculate(request=mocked_request)
    
        assert excinfo.value == "Poorly Body Formated"