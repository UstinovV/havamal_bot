# -*- coding: utf-8 -*-
import sys
import time
import random
import datetime
import telepot
import sqlite3


def connect_db():
    return sqlite3.connect('words.db')


def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print 'Got command: %s' % command

    if command == '/word':
        bot.sendMessage(chat_id, 'Слово Высокого')
    elif command == '/words':
        word_id = random.randint(1,164)
        params =(word_id,)
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM words where id=?', params)
        fetch = cursor.fetchone()
        result = fetch[1].encode('utf-8').strip()
        bot.sendMessage(chat_id, result)

bot = telepot.Bot('172517273:AAHkVkQoe-FvfVXPi6uUeDjR4N_s_gFQN3U')
bot.notifyOnMessage(handle)
print 'I am listening ...'

while 1:
    time.sleep(10)