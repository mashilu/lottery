# -*- coding=utf-8 -*-

import itertools
from database.mysqldb import MySqlDb


def truncate_table(dbconn, table_name):
	dbconn.exe_truncate(table_name)


def save_data(dbconn, result):
	# insert new data
	sql_insert = "insert into lottery.ssqCombination(id, red1,  \
			red2, red3, red4, red5, red6, blue)  \
			values(%s, %s, %s, %s, %s, %s, %s, %s)" % tuple(result)
	dbconn.exe_insert(sql_insert)


def check_data(dbconn, count):
	# check number of data inserted with count
	sql_count = "select count(1) from lottery.ssqCombination"
	dbconn.exe_sql(sql_count)
	# return type of fetch_one is tuple
	dbcnt = dbconn.fetch_one()[0]
	print(dbcnt, count)
	if count == dbcnt:
		print("insert operation is finished successfully")
	else:
		print("insert operation is finished with error")

if __name__ == "__main__":
	db = MySqlDb(host='localhost', port=3306, user='root', passwd='root', db='lottery', charset='UTF8')
	db.conndb()
	truncate_table(db, "lottery.ssqCombination")
	# total record quantity
	get_count = 0

	for reds in [x for x in itertools.combinations(range(1, 34), 6)]:
		for blue in range(1, 17):
			balls = list(reds)
			balls.append(blue)
			print(balls)
			get_count += 1
			balls.insert(0, get_count)
			save_data(db, balls)
			check_data(db, get_count)

	db.close()
