#!/usr/bin/python3
''' Will list all states from the database hbtn_0e_0_usa '''

import sys
import MySQLdb

if __name__ == "__main__":

    argIn = [sys.argv[1], sys.argv[2], sys.argv[3]]

    DB = MySQLdb.connect(user=argIn[0], passwd=argIn[1], db=argIn[2])
    CR = DB.cursor()

    CR.execute('SELECT * FROM `states` ORDER BY id ASC')
    data = CR.fetchall()

    for i in data:
        print(i)

    CR.close()
    DB.close()
