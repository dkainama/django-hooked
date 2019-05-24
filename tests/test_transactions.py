# -*- coding: utf-8 -*-
from unittest import skip

from django.test import TestCase

from hooked.models import TransactionStatus, WebHookTransaction


class TestTransactionsOnModel(TestCase):
    def test_check_transaction_enum_status(self):
        self.assertEqual(WebHookTransaction.STATUS.AWAITING, TransactionStatus.AWAITING)
        self.assertEqual(WebHookTransaction.STATUS.PROGRESS, TransactionStatus.PROGRESS)
        self.assertEqual(
            WebHookTransaction.STATUS.PROCESSED, TransactionStatus.PROCESSED
        )
        self.assertEqual(WebHookTransaction.STATUS.FAILED, TransactionStatus.FAILED)

    def test_init_transaction_hook(self):
        # setup hook
        hook = WebHookTransaction()
        # asserts
        self.assertEqual(hook.current_status, TransactionStatus.AWAITING)

    def test_body_and_meta_transaction_hook(self):
        # setup hook
        hook = WebHookTransaction()
        # set request data
        hook.body = {'hooked': True}
        hook.meta = {'user-agent': 'pirateOS/1.0'}

        # asserts
        self.assertEqual(hook.current_status, TransactionStatus.AWAITING)
        self.assertEqual(hook.body, {'hooked': True})
        self.assertEqual(hook.meta, {'user-agent': 'pirateOS/1.0'})
