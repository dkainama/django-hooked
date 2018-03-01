import uuid

import factory
from hooked.models import WebHookClientApp


class WebHookClientAppFactory(factory.Factory):
    class Meta:
        model = WebHookClientApp

    name = 'Pirate'
    identifier = uuid.uuid4()
    secret = 'pirate'
