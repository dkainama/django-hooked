# -*- coding: utf-8 -*-

from enum import IntEnum

from django.db import models
from django.utils import timezone
from jsonfield import JSONField


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
    
    # status of transaction { TransactionStatus }
    status = models.IntegerField(choices=STATUS, default=STATUS.AWAITING)
    
    # flags
    modified = models.DateTimeField()
    created = models.DateTimeField(default=timezone.now())
    
    @property
    def current_status(self):
        return TransactionStatus(self.status)
    
    def __unicode__(self):
        return u'{0}'.format(self.date_event_generated)
