from typing import Dict
from .calculator_1 import Calculator1
from pytest import raises


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

def test_calculate():
    calculator1 = Calculator1()
    mock_request = MockRequest(body={"number": 1})

    response = calculator1.calculate(mock_request.json)
    
    #Testing the format
    assert "data" in response
    assert "Calculator" in response["data"]
    assert "result" in response["data"]

    #Response assertivity
    assert response["data"]["result"] == 14.25
    assert response["data"]["Calculator"] == 1

def test_calculate_with_body_error():
    calculator1 = Calculator1()
    mocket_request = MockRequest(body={"something": 2})

    with raises(Exception) as excinfo:
        response = calculator1.calculate(mocket_request.json)
        
        assert excinfo.value == "Poorly formated body"