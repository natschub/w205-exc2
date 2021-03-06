import sys

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

if len(sys.argv) !=2:
	cur.execute("SELECT word, count from tweetwordcount order by word ASC")
	records=cur.fetchall()
	for rec in records:
		print ( rec[0], rec[1])
	conn.commit()
	conn.close

else:
	word = sys.argv[1]

	cur.execute("SELECT word, count from tweetwordcount order by word ASC")
	records=cur.fetchall()
	
	for rec in records:
		if rec[0]==word:
			print (rec[0], rec[1])

	conn.commit()
	conn.close
