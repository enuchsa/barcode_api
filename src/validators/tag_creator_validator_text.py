from src.errors.errors_types.http_unprocessable_enitity import HttpUnprocessableEntityError
from .tag_creator_validator import tag_creator_validator

class MockRequest:
    def __init__(self, json) -> None:
        self.json = json
        
    def test_tag_creator_validator():
        req = MockRequest(json={"product_code": "12345"})
        response = tag_creator_validator(req)
        
    def test_tag_creator_validator_with_error():
        req = MockRequest(json={ "produt_code": 12345 })
        
        try:
            tag_creator_validator(req)
            assert False
        except Exception as excepttion:
            assert isinstance(excepttion, HttpUnprocessableEntityError)