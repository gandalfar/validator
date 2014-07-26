# -*- coding: utf-8 -*-
from validator.views import TextFormValidatorView
import pytest

@pytest.mark.client
def test_form_text_input(rf, client):
    response = client.post('/', {'content': '{"data": []}'})
    assert 'Validation results' in response.content, "Form didn't validate"


def test_form_invalid_json(rf):
    request = rf.post('/', {'content': '{invalid json;'})
    view = TextFormValidatorView.as_view()
    response = view(request)
    assert 'Invalid JSON Input' in response.content, "Form didn't raise invalid JSON error"


def test_form_valid_input(rf):
    request = rf.post('/', {'content': open('validator/tests/assets/simple_example.json').read()})
    view = TextFormValidatorView.as_view()
    response = view(request)
    assert 'Successfully Validated Input JSON' in response.content


def test_form_upload_file(rf):
    with open('validator/tests/assets/simple_example.json') as fp:
        request = rf.post('/', {'file': fp})
    view = TextFormValidatorView.as_view()
    response = view(request)
    assert 'Successfully Validated Input JSON' in response.content
