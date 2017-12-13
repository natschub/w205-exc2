import sys

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()


if len(sys.argv) !=3:
	print "function requres two inputs- please add two input in ascending order with a space between"

else:
	k1=int(sys.argv[1])
	k2=int(sys.argv[2])

	cur.execute("SELECT word, count from tweetwordcount order by count DESC")
	records=cur.fetchall()
	records=filter(lambda x: x[1] >=k1, records)
	records=filter(lambda x: x[1] <=k2, records)	
	for rec in records:
		print (rec[0], rec[1])

	conn.commit()
	conn.close
