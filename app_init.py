# Tasks to initialise the application

from textblob.packages import nltk

MIN_CORPORA = [
  'brown',  # Required for FastNPExtractor
  'punkt',  # Required for WordTokenizer
  'wordnet' # Required for lemmatization
]

def download_corpora():
  for each in MIN_CORPORA:
    print('Downloading "{0}"'.format(each))
    nltk.download(each)

if __name__ == "__main__":
   download_corpora()
