#!/usr/bin/python3
''' Will list all states from the database hbtn_0e_0_usa '''

import MySQLdb
import sys
import re

if __name__ == "__main__":

    argIn = [sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]]
    query = '''SELECT * FROM `states` \
            HAVING `name`= '{:s}'\
            ORDER BY `id` ASC'''
    state = argIn[3]

    DB = MySQLdb.connect('localhost', argIn[0], argIn[1], argIn[2], port=3306)
    CR = DB.cursor()

    CR.execute(query.format(state))
    data = CR.fetchall()

    for i in data:
        if (i[1] == state):
            print(i)

    CR.close()
    DB.close()
