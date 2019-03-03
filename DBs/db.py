import sqlite3
from lxml import html
import requests
import datetime

page = requests.get('http://jobs.bg/index.php')
tree = html.fromstring(page.content)
jobs = tree.xpath('//span[@style="color:#8dbe35;font-weight:bold;"]/text()')
now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")
time = now.strftime("%H:%M:%S")
conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute("INSERT INTO jobstats (date, time, totaljobs, newjobs) VALUES (?, ?, ?, ?)",(date, time, jobs[0], jobs[1]))
conn.commit()
