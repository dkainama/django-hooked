# -*- coding: utf-8 -*-
from django.views import View

from hooked.models import TransactionStatus
from hooked.receivers import WebHookReceiverMixin


class WebHookView(WebHookReceiverMixin, View):
    def run_hook_transaction(self, obj, event, *args, **kwargs):
        print('running some shit')
        obj.status = TransactionStatus.PROCESSED
        obj.save()
