#!/usr/bin/env python
# coding=utf-8

from mailjet.client import build_headers, build_body_and_url, api_call, parse_response

def test_build_headers():
    assert build_headers() == {'Content-type': 'application/json'}
    assert build_headers(extra_headers={'foo': 'bar'}) == {
        'Content-type': 'application/json', 'foo': 'bar'}

def test_build_body_and_url():
    raise NotImplementedError

def test_api_call():
    raise NotImplementedError

def test_parse_response():
    raise NotImplementedError
