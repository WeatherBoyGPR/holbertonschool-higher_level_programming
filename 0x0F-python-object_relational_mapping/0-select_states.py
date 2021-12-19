#!/usr/bin/python3
# Lists states from database hbtn_0e_0_usa

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM `states`")
    for line in cur.fetchall():
        print(line)
    cur.close()
    db.close()
