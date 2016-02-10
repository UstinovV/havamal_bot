# -*- coding: utf-8 -*-

#telegram framework
import telepot
from pprint import pprint

# all the imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

# configuration
DATABASE = 'words.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)

bot = telepot.Bot('TOKEN')

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print content_type, chat_type, chat_id
    bot.sendMessage(40172523, 'Слово Высокого')
    pprint(msg)

@app.before_request
def before_request():
    g.db = connect_db()


@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()


@app.route('/')
def hello_world():
    #bot = telepot.Bot(TOKEN)
    # print bot.getMe()
    # response = bot.getUpdates()
    # pprint(response)
    cur = g.db.execute('SELECT * FROM words')
    entries = [dict(id=row[0], word=row[1]) for row in cur.fetchall()]
    bot.notifyOnMessage(handle)
    #bot.sendMessage(40172523, entries[0]['word'].encode('utf-8').strip())

    return 'Hello World!'


@app.route('/words/', methods=['GET'])
def random_word():
    cur = g.db.execute('SELECT * FROM words')
    entries = [dict(id=row[0], word=row[1]) for row in cur.fetchall()]
    print entries
    return 'random_word'


@app.route('/word/<int:word_id>/', methods=['GET'])
def word_by_id(word_id):
    return "word:{0}".format(word_id)

if __name__ == '__main__':
    app.run()
