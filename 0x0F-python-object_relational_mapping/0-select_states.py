#!/usr/bin/python3
# Will list all states from the database hbtn_0e_0_usa

import MySQLdb
import sys

argIn = [sys.argv[1], sys.argv[2], sys.argv[3]]

DB = MySQLdb.connect('localhost', argIn[0], argIn[1], argIn[2])
CR = DB.cursor()

CR.execute('SELECT * FROM states ORDER BY id ASC')
data = CR.fetchall()

for i in data:
    print(i)

CR.close()
DB.close()
