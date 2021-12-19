#!/usr/bin/python3
# Will list states with name same as argument

import MySQLdb
import sys

if __name__ == "__main__":
    s = sys.argv[4]
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset='utf8')
    cur = db.cursor()
    cur.execute("SELECT * FROM `states`\
            WHERE name LIKE %s ORDER BY id ASC", [s])
    for line in cur.fetchall():
        print(line)
    cur.close()
    db.close()
