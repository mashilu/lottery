# -*- coding:utf-8 -*-

import urllib.request

from database.mysqldb import MySqlDb
from htmlparser.SsqHtmlParser import SsqHTMLParser


def truncate_table(dbconn, table_name):
	dbconn.exe_truncate(table_name)


def save_data(dbconn, result):
	# insert new data
	for curr_result in result:
		sql_insert = "insert into lottery.ssqHistory(no, red1, \
				red2, red3, red4, red5, red6, blue1) \
				values(%s, %s, %s, %s, %s, %s, %s, %s)" % tuple(curr_result)
		dbconn.exe_insert(sql_insert)


def check_data(dbconn, count):
	# check number of data inserted with count
	sql_count = "select count(1) from lottery.ssqHistory"
	dbconn.exe_sql(sql_count)
	# return type of fetch_one is tuple
	dbcnt = dbconn.fetch_one()[0]
	print(dbcnt, count)
	if count == dbcnt:
		print("insert operation is finished successfully")
	else:
		print("insert operation is finished with error")

if __name__ == "__main__":
	base_url = "http://www.3dcp.cn/zs/gonggao.php?type=ssq&year="

	db = MySqlDb(host='localhost', port=3306, user='root', passwd='root', db='lottery', charset='UTF8')
	db.conndb()
	truncate_table(db, "lottery.ssqHistory")

	# total record quantity
	get_count = 0
	for url in [base_url + str(x) for x in range(2002, 2017, 1)]:
		content = urllib.request.urlopen(url).read()
		ball = SsqHTMLParser()
		ball.feed(content.decode("GB2312"))
		save_data(db, ball.result)
		get_count += len(ball.result)

	check_data(db, get_count)

	db.close()
