#Bottle skeleton app for Heroku

A mini [bottle](http://bottlepy.org/) skeleton app for deployment on [heroku](http://heroku.com)

##Deploy to Heroku
Clone and add to git

    $ git clone git@github.com:alyssaq/bottle-heroku-skeleton.git
    $ git init
    $ git add .
    $ git commit -m "init"

Test with foreman

    $ foreman start
    
Push to heroku

    $ heroku login
    $ git push heroku master
    $ heroku open //Open the app in the browser

##Develop locally

Install requirements into a virtualenv:

    $ virtualenv env
    $ source env/bin/activate
    $ pip install -r requirements.txt
    $ deactivate //stop virtualenv when you are done

##Running locally

    $ python app.py 8888 // Specify a port
    $ python app.py      // Use default 8080 port

Open browser at `http://localhost:8080`

##License
MIT License