from django.contrib import admin

from hooked.admin import HooksClientApps, HooksTransactions
from hooked.models import WebHookClientApp, WebHookTransaction

# Register your models here.
admin.site.register(WebHookClientApp, HooksClientApps)
admin.site.register(WebHookTransaction, HooksTransactions)
