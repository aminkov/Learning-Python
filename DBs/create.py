import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute('''CREATE TABLE jobstats
             (date text, totaljobs int, newjobs int)''')
c = conn.cursor()