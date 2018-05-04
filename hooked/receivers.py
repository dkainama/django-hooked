# -*- coding: utf-8 -*-
import json

from django.views.decorators.csrf import csrf_exempt

from .http import HookedReponse, HookedRequest
from .models import WebHookClientApp, WebHookTransaction


class WebHookReceiverMixin(object):
    
    # handles transaction
    def run_hook_transaction(self, model, event, *args, **kwargs):
        pass
    
    # dispatch webhook receiver
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        
        if request.method == 'POST':
            
            # hook request
            hooked_request = HookedRequest(request)
            
            # check if app_id exists in request <=> 403
            if not hooked_request.app_id:
                return HookedReponse.NotAuthorized
            
            # get app
            app = WebHookClientApp.objects.filter(
                identifier=hooked_request.app_id).first()

            # check if token exists in request <=> 401
            if app.need_authorization:
                if not hooked_request.token:
                    return HookedReponse.NotAuthorized        
                
                is_valid = hooked_request.is_token_valid(app.secret)
                # now check valid token and get from app <=> 403
                if not is_valid:
                    return HookedReponse.Forbidden
            
            # convert body from bytes to str compatible
            body = hooked_request.body
            headers = {}  # FIXME filter  X-HTTP headers only#
            
            # get event and run transaction
            event = hooked_request.event
            
            # secure so start transaction
            transaction = WebHookTransaction.objects.create(
                body=body, meta=headers, app=app, event=event
            )
            
            self.run_hook_transaction(transaction, event)
            
            return HookedReponse.Authorized
        else:
            return HookedReponse.Forbidden
