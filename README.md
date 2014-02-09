#Bottle skeleton for Heroku with scientific packages

A mini [bottle](http://bottlepy.org/) skeleton app for deployment on [heroku](http://heroku.com).    
Sample deployment with numpy, pandas, textblob (with some nltk corpora).

##Deploy to Heroku
Clone and add to git
```sh
  $ git clone git@github.com:alyssaq/bottle-heroku-skeleton.git
  $ git init
  $ git add .
  $ git commit -m "init"
```
Specify custom buildpack and push to heroku
```sh
  $ heroku login
  $ heroku config:set BUILDPACK_URL=https://github.com/dbrgn/heroku-buildpack-python-sklearn/
  $ git push heroku master
  $ heroku open #Open the app in the browser
```
##Develop locally

Install requirements into a virtualenv:

```sh
  $ virtualenv env
  $ source env/bin/activate
  $ pip install -r requirements.txt
  $ deactivate # Stop virtualenv when you are done
```

##Running locally

Locally:

```sh
  $ python app.py 8888 # Specify a port
  $ python app.py      # Use default 8080 port
```

Using Foreman:
```sh
  $ foreman start
```
Open browser at `http://0.0.0.0:8080`

##License
MIT License