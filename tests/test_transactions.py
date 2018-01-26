# -*- coding: utf-8 -*-

from django.test import TestCase

from hooked.transactions import TransactionStatus, WebHookTransaction


class TestTransactionsOnModel(TestCase):
    def test_check_transaction_enum_status(self):
        self.assertEquals(WebHookTransaction.STATUS.AWAITING, TransactionStatus.AWAITING)
        self.assertEquals(WebHookTransaction.STATUS.PROGRESS, TransactionStatus.PROGRESS)
        self.assertEquals(WebHookTransaction.STATUS.PROCESSED, TransactionStatus.PROCESSED)
        self.assertEquals(WebHookTransaction.STATUS.FAILED, TransactionStatus.FAILED)
        
        
    def test_init_transaction_hook(self):
        # setup hook
        hook = WebHookTransaction()
        # asserts
        self.assertEquals(hook.current_status, TransactionStatus.AWAITING)


    def test_body_and_meta_transaction_hook(self):
        # setup hook
        hook = WebHookTransaction()
        # set request data
        hook.body = {'hooked': True }
        hook.meta = {'user-agent': 'pirateOS/0.1'}
        
        # asserts
        self.assertEquals(hook.current_status, TransactionStatus.AWAITING)
        self.assertEquals(hook.body, {'hooked': True })
        self.assertEquals(hook.meta, {'user-agent': 'pirateOS/0.1'})
