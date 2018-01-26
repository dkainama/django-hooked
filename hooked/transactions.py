# -*- coding: utf-8 -*-

from enum import Enum

# from django.contrib.postgres.fields import JSONField
from django.db import models
from django.utils import timezone


class TransactionStatus(Enum):
    AWAITING = 1
    PROGRESS = 2
    PROCESSED = 3
    FAILED = 4

    def __str__(self):
        return "%s" % self.value


class WebHookTransaction(models.Model):
    
    STATUS = TransactionStatus
    
    # request body & meta
    body = models.TextField()
    meta = models.TextField()
    
    # status of transaction { TransactionStatus }
    status = models.IntegerField(choices=STATUS, default=STATUS.AWAITING.value)
    
    # flags
    modified = models.DateTimeField()
    created = models.DateTimeField(default=timezone.now())
    
    
    @property
    def current_status(self):
        TransactionStatus(self.status)
    
    def __unicode__(self):
        return u'{0}'.format(self.date_event_generated)
