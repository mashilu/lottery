import pymysql


class MyDb:
	def __init__(self, **kwargs):
		self.conn_str = kwargs
		print(self.conn_str)
		self.conn = 0
		self.curr = 0

	def conndb(self):
		# 字典作为参数传递！！
		self.conn = pymysql.connect(**self.conn_str)
		self.curr = self.conn.cursor()

	def exe_query(self, sql):
		self.curr.execute(sql)

	def exe_insert(self, sql):
		self.curr.execute(sql)
		self.conn.commit()

	def close(self):
		self.conn.close()


if __name__ == "__main__":
	db = MyDb(host='localhost', port=3306, user='root', passwd='root', db='lottery', charset='UTF8')
	db.conndb()
	test = [1, 1]
	sql1 = "select * from dltCombination where %d = %d" % tuple(test)
	db.exe_query(sql1)

