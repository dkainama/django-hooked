# -*- coding: utf-8 -*-

from enum import Enum


class TransactionStatus(Enum):
    AWAITING = 1
    PROGRESS = 2
    PROCESSED = 3
    FAILED = 4

    def __str__(self):
        return "%s" % self.value


class HookedTransaction:
    STATUS = TransactionStatus
