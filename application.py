import os
import ssl
import feedparser
from flask import Flask, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://{username}:{password}@db:27017/{db}".format(
    username=os.environ['MONGODB_USERNAME'],
    password=os.environ['MONGODB_PASSWORD'],
    db=os.environ['MONGO_INITDB_DATABASE']
)

mongo = PyMongo(app)


def get_feeds():
    feeds = []

    filepath = 'feeds.txt'
    with open(filepath) as fp:
        for feed in fp:
            feeds.append(feed)

    return feeds

@app.route('/')
def index():
    mongo.db.feeds.find_one()
    if hasattr(ssl, '_create_unverified_context'):
        ssl._create_default_https_context = ssl._create_unverified_context

    feeds = get_feeds()

    data = [feedparser.parse(feed) for feed in feeds]

    return render_template('index.html', feeds=data)

