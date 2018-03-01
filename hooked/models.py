# -*- coding: utf-8 -*-
import uuid
from enum import IntEnum

from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone

from jsonfield import JSONField

from .tokens import generate_random_secret


class WebHookClientApp(models.Model):
    
    # name
    name = models.CharField(u'Name', max_length=255)
    
    # app identifier
    identifier = models.UUIDField(
        u'Identifier', default=uuid.uuid4, editable=False
    )
    
    # Signature / HMAC shared secret
    secret = models.CharField(
        u'Shared secret', max_length=255,
        editable=False,
        default=generate_random_secret
    )
    
    # options
    need_authorization = models.BooleanField(
        u'Secure endpoint for this app?', default=True
    )
     
    # flags
    modified = models.DateTimeField(u'Modified on', null=True, blank=True)
    created = models.DateTimeField(u'Created at', default=timezone.now)

    def __unicode__(self):
        return u'{0}'.format(self.created)
    
    class Meta:
        verbose_name = 'App'


class TransactionStatus(IntEnum):
    AWAITING = 1
    PROGRESS = 2
    PROCESSED = 3
    FAILED = 4

    def __str__(self):
        return "%s" % self.value


class WebHookTransaction(models.Model):
    
    STATUS = TransactionStatus
    
    # request body & meta
    body = JSONField()
    meta = JSONField()
    
    # app
    app = models.ForeignKey(WebHookClientApp, on_delete=models.CASCADE)
    
    # status of transaction { TransactionStatus }
    status = models.IntegerField(
        choices=((x.value, x.name.title()) for x in STATUS), 
        default=STATUS.AWAITING
    )
    
    # event
    event = models.CharField(
        u'Event', max_length=255,
        editable=False,
    )
    
    # flags
    modified = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(default=timezone.now)
    
    @property
    def signature(self):
        event = self.event
        slug = slugify(self.app.name)
        timestamp = self.created.strftime('%s')
        return "{0}-{1}-{2}".format(event, slug, timestamp)
        
    @property
    def current_status(self):
        return TransactionStatus(self.status)
    
    def __str__(self):
        return "%s" % self.signature
    
    def __unicode__(self):
        return u'{0}'.format(self.created)
        
    class Meta:
        verbose_name = 'Transaction'
