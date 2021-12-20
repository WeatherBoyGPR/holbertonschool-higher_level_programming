#!/usr/bin/python3
""" SQL Injection proof, retrieves states specified by last arg """

import sys
import MySQLdb

if __name__ == "__main__":
    s = sys.argv[4]
    sta = "SELECT * FROM `states` ORDER BY id ASC"
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset='utf8')
    cur = db.cursor()
    cur.execute(sta)
    for line in cur.fetchall():
        if line[1] == s:
            print(line)
    cur.close()
    db.close()
