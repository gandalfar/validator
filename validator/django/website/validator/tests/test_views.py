# -*- coding: utf-8 -*-
from validator.views import TextFormValidatorView


def test_form_text_input(rf):
    request = rf.post('/', {'content': '{"data": []}'})
    view = TextFormValidatorView.as_view()
    response = view(request)
    assert 'Validation results' in response.content, "Form didn't validate"


def test_form_invalid_json(rf):
    request = rf.post('/', {'content': '{invalid json;'})
    view = TextFormValidatorView.as_view()
    response = view(request)
    assert 'Invalid JSON Input' in response.content, "Form didn't validate"
