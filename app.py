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
import sys
from textblob.packages import nltk

bottle.debug(True)

MIN_CORPORA = [
  'brown',  # Required for FastNPExtractor
  'punkt',  # Required for WordTokenizer
  'wordnet' # Required for lemmatization
]

def download_lite():
  for each in MIN_CORPORA:
    print('Downloading "{0}"'.format(each))
    nltk.download(each)

download_lite()

@get('/')
def index():
  response.content_type = 'text/plain; charset=utf-8'
  
  ret =  'Hello world, I\'m {0}!\n\n'.format(os.getpid())

  sentence = 'Now is better than never.'
  ret += 'Testing TextBlob ngram with sentence: \n "{0}"'.format(sentence)
  blob = TextBlob(sentence)
  for word_list in blob.ngrams(n=3):
    ret += ('\n' + ' '.join(word_list))
  
  data = pd.DataFrame({'A': np.random.randn(3), 'B': np.random.randn(3)})
  ret += '\nTesting numpy and pandas: \n {0} \n'.format(data.to_json())
    
  ret += '\nEnvironment vars:\n'

  for k, v in env.iteritems():
    if 'bottle.' in k:
      continue
    ret += '%s=%s\n' % (k, v)

  return ret

app_port = argv[1] if len(argv) > 1 else 8080
bottle.run(host='0.0.0.0', port=app_port)