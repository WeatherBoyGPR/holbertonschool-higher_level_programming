#!/usr/bin/python3
# Will list all cities in specified states from the database hbtn_0e_4_usa

import MySQLdb
import sys
import re

if __name__ == "__main__":

    argIn = [sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]]
    query = '''\
            SELECT *\
            FROM `cities`\
            INNER JOIN `states`\
                ON `states`.`id`=`cities`.`state_id`\
            HAVING `states`.`name` = '{}'\
            ORDER BY `cities`.`id` ASC\
            '''
    DB = MySQLdb.connect('localhost', argIn[0], argIn[1], argIn[2], port=3306)
    CR = DB.cursor()

    CR.execute(query.format(argIn[3]))
    data = CR.fetchall()

    res = []
    for i in data:
        res.append(i[2])

    print(str(res).replace('\'', '')[1:-1])
    CR.close()
    DB.close()
