#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from os import environ as env
from sys import argv

import bottle
from bottle import default_app, request, route, response, get

from textblob import TextBlob
import pandas as pd
import numpy as np

#import appconfig

bottle.debug(True)

@get('/')
def index():
  response.content_type = 'text/plain; charset=utf-8'
  blob = TextBlob("Now is better than never.")
  data = pd.DataFrame({'A': np.random.randn(3), 'B': np.random.randn(3)})

  ret =  'Hello world, I\'m {0}!\n\n'.format(os.getpid())
  for word_list in blob.ngrams(n=3):
    ret += ' '.join(word_list)

  ret += '\n'
  ret += data.to_json()
  ret += '\nRequest vars:\n'
  for k, v in request.environ.iteritems():
    if 'bottle.' in k:
      continue
    ret += '%s=%s\n' % (k, v)

  ret += '\n'
  ret += 'Environment vars:\n'

  for k, v in env.iteritems():
    if 'bottle.' in k:
      continue
    ret += '%s=%s\n' % (k, v)

  return ret

app_port = argv[1] if len(argv) > 1 else 8080
bottle.run(host='0.0.0.0', port=app_port)