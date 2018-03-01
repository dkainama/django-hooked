# -*- coding: utf-8 -*-
from django.apps import AppConfig


class HookedAppConfig(AppConfig):
    name = 'hooked'
    verbose_name = 'Webhooks'
