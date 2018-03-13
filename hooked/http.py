# -*- coding: utf-8 -*-
from django.http import JsonResponse

from .tokens import validate_token


class HookedRequest:
    def __init__(self, request):
        self.request = request
    
    def is_token_valid(self, secret):            
        return validate_token(secret, str(self.body), self.token)
    
    @property
    def body(self):
        return self.request.body
        
    @property
    def headers(self):
        return self.request.META
    
    @property
    def app_id(self):
        return self.headers.get(HookedRequest.Headers.HookedAppId)
        
    @property
    def token(self):
        return self.headers.get(HookedRequest.Headers.HookedToken)
        
    @property
    def event(self):
        return self.headers.get(HookedRequest.Headers.HookedEvent)
    
    class Headers:
        HookedAppId = 'HTTP_X_HOOKED_APP_ID'
        HookedToken = 'HTTP_X_HOOKED_TOKEN'
        HookedEvent = 'HTTP_X_HOOKED_EVENT'


class HookedReponse:
    NotAuthorized = JsonResponse({'status': 'Not Authorized'}, status=401)
    Forbidden = JsonResponse({'status': 'Forbidden'}, status=403)
    Authorized = JsonResponse({'status': 'Authorized'}, status=201)
