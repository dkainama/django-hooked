# -*- coding: utf-8 -*-
from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory
from rest_framework.test import APIRequestFactory  # stub with DRF

from hooked.http import HookedRequest


class WebHookRequestFactory(APIRequestFactory):

    def __init__(self, app_id=None, token=None, event='default', *args, **kwargs):
        super(WebHookRequestFactory, self).__init__(*args, **kwargs)
        self.token = token
        self.app_id = app_id
        self.event = event
        
    def build_params(self):
        params = {}
        if self.token:
            params[HookedRequest.Headers.HookedToken] = self.token
        if self.app_id:
            params[HookedRequest.Headers.HookedAppId] = self.app_id
        if self.event:
            params[HookedRequest.Headers.HookedEvent] = self.event
        
        return params

    def perform(self, data):
        user = AnonymousUser()
        params = self.build_params()
        req = self.post('/webhooks', data=data , format='json', **params)        
        req.user = user
        return req
