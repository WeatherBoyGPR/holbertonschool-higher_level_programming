#!/usr/bin/python3
''' Will list all cities from the database hbtn_0e_4_usa '''

import MySQLdb
import sys
import re

if __name__ == "__main__":

    argIn = [sys.argv[1], sys.argv[2], sys.argv[3]]
    query = '''\
            SELECT  `cities`.`id`, `cities`.`name`, `states`.`name`\
            FROM `cities`\
            INNER JOIN `states` ON `states`.`id`=`cities`.`state_id`\
            ORDER BY `cities`.`id` ASC\
            '''
    DB = MySQLdb.connect('localhost', argIn[0], argIn[1], argIn[2], port=3306)
    CR = DB.cursor()

    CR.execute(query)
    data = CR.fetchall()

    for i in data:
        print(i)

    CR.close()
    DB.close()
