# -*- coding: utf-8 -*-

from django.db import models
from django.test import TestCase

from hooked.transactions import HookedTransaction, TransactionStatus


class Message(models.Model, HookedTransaction):
    pass


class TestTransactionsOnModel(TestCase):
    def test_extending_message_with_transaction_mixin(self):
        self.assertEquals(
            HookedTransaction.STATUS.AWAITING,
            TransactionStatus.AWAITING)
        self.assertEquals(
            HookedTransaction.STATUS.PROGRESS,
            TransactionStatus.PROGRESS)
        self.assertEquals(
            HookedTransaction.STATUS.PROCESSED,
            TransactionStatus.PROCESSED)
        self.assertEquals(
            HookedTransaction.STATUS.FAILED,
            TransactionStatus.FAILED)
