from __future__ import print_function

import json

print('Loading function')

def lambda_handler(event, context):
    print('hello world.')
    return 'function is update.'
