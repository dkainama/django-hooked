# -*- coding: utf-8 -*-

import base64
import hmac
import os
from hashlib import sha256

from django.utils.encoding import force_bytes


def generate_random_secret():
    return sha256(os.urandom(256)).hexdigest()  


def generate_token(key, msg):
    
    # check for encode methods => base64 body results in serious 
    # problems when double encoding back from PHP.
    key = str(key.decode('utf8'))
    decoded = str(msg.decode('utf8'))
    
    token = hmac.new(force_bytes(key), digestmod=sha256)
    token.update(decoded)  # explicit update
    
    print('generate_token:msg:decoded', decoded)
    print('generate_token:before', token.hexdigest())
    
    return token.hexdigest()


def validate_token(key, msg, token):
    key = str(key)
    sig = generate_token(key=key, msg=msg)
    return hmac.compare_digest(force_bytes(sig), force_bytes(token))
