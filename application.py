import ssl
import feedparser
from flask import Flask, render_template


app = Flask(__name__)


def get_feeds():
    feeds = []

    filepath = 'feeds.txt'
    with open(filepath) as fp:
        for feed in fp:
            feeds.append(feed)

    return feeds

@app.route('/')
def index():
    if hasattr(ssl, '_create_unverified_context'):
        ssl._create_default_https_context = ssl._create_unverified_context

    feeds = get_feeds()

    data = [feedparser.parse(feed) for feed in feeds]

    #for feed in feeds:
    #    d = feedparser.parse(feed)
    #    for i in range(10):
    #        entry = f'{d.entries[i].title} {d.entries[i].published} {d.entries[i].link}'
    #        response += f'/n{entry}'
    
    
 
    return render_template('index.html', feeds=data)

