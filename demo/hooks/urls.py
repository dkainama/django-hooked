
from django.urls import path

from .views import WebHookView

urlpatterns = [
    path( r'webhooks/', WebHookView.as_view(), name='webhooks'),
]
