# -*- coding: utf-8 -*-
import base64
import json
import uuid
from unittest import skip

from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory, TestCase
from django.utils.encoding import force_bytes

from hooked.models import (TransactionStatus, WebHookClientApp,
                           WebHookTransaction)
from hooked.tokens import generate_token

from .factories.requests import WebHookRequestFactory
from .factories.views import WebHookViewFactory


class TestReceiversMiddelware(TestCase):
    def setUp(self):
        self.payload = str('{"foo": 1}')
        self.app = WebHookClientApp.objects.create(
            name='Pirate', identifier=uuid.uuid4(), 
            secret="pirate", need_authorization=True
        )
    
    # returns 401 if X_HOOKED_TOKEN is missing
    def test_transaction_hook_wihout_token_and_return_401(self):
        request = WebHookRequestFactory().perform(data=self.payload)
        response = WebHookViewFactory.as_view()(request)
        self.assertEqual(response.status_code, 401)
    
    # roken is invalid
    def test_invalid_authorized_request_transaction_hook_and_return_403(self):
        request = WebHookRequestFactory(
            token='wrong', app_id=self.app.identifier
        ).perform(data=self.payload)
        
        response = WebHookViewFactory.as_view()(request)
        self.assertEqual(response.status_code, 403)
    
    # everything is OK, return 200
    def test_valid_authorized_request_transaction_hook_and_return_201(self):
        token = generate_token(self.app.secret, self.payload)
        
        request = WebHookRequestFactory(
            token=token, app_id=self.app.identifier
        ).perform(data=self.payload)
        
        response = WebHookViewFactory.as_view()(request)
        self.assertEqual(response.status_code, 201)
