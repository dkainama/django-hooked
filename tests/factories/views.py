from django.views import View

from hooked.http import HookedReponse
from hooked.receivers import WebHookReceiverMixin

from .models import WebHookClientAppFactory


class WebHookViewFactory(WebHookReceiverMixin, View):
    
    def run_hook_transaction(self, obj, event, *args, **kwargs):
        print('running transaction and more')
