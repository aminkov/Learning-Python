import sqlite3
from lxml import html
import requests
import datetime

page = requests.get('http://jobs.bg/index.php')
tree = html.fromstring(page.content)
jobs = tree.xpath('//span[@style="color:#8dbe35;font-weight:bold;"]/text()')

print(jobs[0])
print(jobs[1])
conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute("INSERT INTO jobstats (date, totaljobs, newjobs) VALUES (?, ?, ?)",(datetime.datetime.now(), jobs[1], jobs[0]))
conn.commit()
