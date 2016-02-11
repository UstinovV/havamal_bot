# -*- coding: utf-8 -*-
import sys
import time
import random
import telepot
import sqlite3

TOKEN = sys.argv[1]  # get token from command-line


def connect_db():
    return sqlite3.connect('words.db')


def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print 'Got command: %s' % command
    conn = connect_db()
    cursor = conn.cursor()
    if command == '/words':
        word_id = random.randint(1,164)
        params = (word_id,)
        cursor.execute('SELECT * FROM words where id=?', params)
        fetch = cursor.fetchone()
        result = fetch[1].encode('utf-8').strip()
        bot.sendMessage(chat_id, result)

    command_list = command.split(" ")
    if command_list[0] == '/word':
        #get first argument from command, it should be a number between 1 and 164
        word_id = command_list[1]
        try:
            word_id = int(word_id)
        except ValueError:
            bot.sendMessage(chat_id, 'Один такого не говорил!!!')
        else:
            if word_id > 164 or word_id < 1:
                bot.sendMessage(chat_id, 'Один такого не говорил!')
            else:
                params = (word_id,)
                cursor.execute('SELECT * FROM words where id=?', params)
                fetch = cursor.fetchone()

                result = fetch[1].encode('utf-8').strip()
                bot.sendMessage(chat_id, result)

bot = telepot.Bot(TOKEN)
bot.notifyOnMessage(handle)
print 'I am listening ...'

while 1:
    time.sleep(10)