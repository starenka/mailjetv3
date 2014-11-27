#!/usr/bin/env python
# coding=utf-8

from mailjet.client import Client

def test_build_headers():
    assert Client.build_headers() == {'Content-type': 'application/json'}
    assert Client.build_headers(extra_headers={'foo': 'bar'}) == {
        'Content-type': 'application/json', 'foo': 'bar'}
