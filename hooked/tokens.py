# -*- coding: utf-8 -*-

import base64
import hmac
import json
import os
from hashlib import sha1, sha256

from django.utils.encoding import force_bytes


def generate_random_secret():
    return sha256(os.urandom(256)).hexdigest()  


def generate_token(key, msg):
    
    key = str(key.decode('utf-8'))
    match = sha1(msg).hexdigest()
    token = hmac.new(force_bytes(key), match, digestmod=sha256).digest()
    
    return base64.b64encode(token).decode()


def validate_token(key, msg, token):
    key = str(key)
    sig = generate_token(key=key, msg=msg)
    return hmac.compare_digest(force_bytes(sig), force_bytes(token))
