#!/usr/bin/python3
""" Lists all cities from database hbtn_0e_4_usa """
import sys
import MySQLdb

if __name__ == "__main__":
    s = sys.argv
    sta = "SELECT * FROM `cities` ORDER BY id ASC"
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=s[1],
            password=s[2],
            db=s[3])
    cur = db.cursor()
    cur.execute(sta)
    for line in cur.fetchall():
        print(line)
    cur.close()
    db.close()
