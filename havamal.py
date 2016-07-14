# -*- coding: utf-8 -*-
# пирамидка ^_^ #
import sys
import time
import redis
import random
import telepot
import sqlite3

from pprint import pprint


def connect_db():
    return sqlite3.connect('havamal.db')


def handle(msg):
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    chat_id = msg['chat']['id']
    command = msg['text']
    print 'Got command: %s' % command
    conn = connect_db()
    cursor = conn.cursor()

    ################################################
    if command == '/runes':
        cursor.execute('SELECT * FROM runes ORDER BY RANDOM() LIMIT 3;')
        fetch = cursor.fetchall()
        result = 'Руны говорят тебе:\n'
        for r in fetch:
            result += "{0} - {1} \n".format(r[1], r[2].encode('utf-8'))
        bot.sendMessage(chat_id, result, reply_markup=show_keyboard)
    ################################################
    if command == '/next':
        last_word = r.get(chat_id)
        # we can use r.incr(chat_id)
        if last_word:
            if last_word == 164:
                last_word = 1
            else:
                last_word = int(last_word) + 1
        else:
            last_word = 1
        r.set(chat_id,last_word)
        cursor.execute('SELECT * FROM words where id=?', (last_word, ))
        fetch = cursor.fetchone()
        result = "Слово {0}:\n".format(last_word)
        result += fetch[1].encode('utf-8').strip()
        bot.sendMessage(chat_id, result, reply_markup=show_keyboard)
    ################################################
    if command == '/words':
        word_id = random.randint(1,164)
        params = (word_id,)
        cursor.execute('SELECT * FROM words where id=?', params)
        fetch = cursor.fetchone()
        result = "Слово {0}:\n".format(word_id)
        result += fetch[1].encode('utf-8').strip()
        bot.sendMessage(chat_id, result, reply_markup=show_keyboard)

    command_list = command.split(" ")
    if command_list[0] == '/word':
        #get first argument from command, it should be a number between 1 and 164
        try:
            word_id = command_list[1]
            word_id = int(word_id)
        except (ValueError, IndexError):
            bot.sendMessage(chat_id, 'Один такого не говорил!', reply_markup=show_keyboard)
        else:
            if word_id > 164 or word_id < 1:
                bot.sendMessage(chat_id, 'Нет такого слова в речах Высокого!', reply_markup=show_keyboard)
            else:
                params = (word_id,)
                cursor.execute('SELECT * FROM words where id=?', params)

                fetch = cursor.fetchone()
                result = "Слово {0}:\n".format(word_id)
                result += fetch[1].encode('utf-8').strip()
                bot.sendMessage(chat_id, result, reply_markup=show_keyboard)

TOKEN = sys.argv[1]  # get token from command-line
show_keyboard = {'keyboard': [['/words', '/runes', '/next']]}



bot = telepot.Bot(TOKEN)
bot.notifyOnMessage(handle)
print 'I am listening ...'

while 1:
    time.sleep(10)