# -*- coding: utf-8 -*-

import sqlite3
from os import walk

f = open('words.txt', 'r')

conn = sqlite3.connect('words.db')
conn.text_factory = str
cursor = conn.cursor()
cursor.execute('DELETE FROM words')

word_id = 1
word = ""
for line in f:

    if (len(line.strip())):
        try:
            i = int(line)
        except ValueError:
            #word += "\n"
            word += line

        else:
            params = (word_id, word)
            print word
            cursor.execute("INSERT INTO words VALUES (?,?)", params)
            conn.commit()
            word_id += 1
            word = ""

    else:
        pass

f.close()
