# -*- coding: utf-8 -*-
import base64
from unittest import skip

from django.test import TestCase
from django.test.client import Client

from hooked.tokens import generate_token, validate_token


class TestHmacTokens(TestCase):
    
    def setUp(self):
        self.secret = 'XXX'
        self.payload = base64.urlsafe_b64encode(b'payload')

    def test_generate_valid_token(self):
        token = generate_token(self.secret, self.payload)
        valid = validate_token(self.secret, self.payload, token)
        
        self.assertTrue(valid);

    def test_generate_invalid_token_wrong_payload(self):
        payload1 = base64.urlsafe_b64encode(b'payload')
        payload2 = base64.urlsafe_b64encode(b'payload-modified-during-request')
        
        token = generate_token(self.secret, payload2)
        valid = validate_token(self.secret, payload1, token)
        
        self.assertFalse(valid);
    
    def test_generate_invalid_token_wrong_secret(self):

        token = generate_token('XXX-WRONG', self.payload)
        valid = validate_token(self.secret, self.payload, token)
        
        self.assertFalse(valid);
