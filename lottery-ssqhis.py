# -*- coding:utf-8 -*-

import urllib.request
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
	def error(self, message):
		pass

	def __init__(self):
		HTMLParser.__init__(self)
		self.is_redspan = ""
		self.is_bluespan = ""
		self.balls = []

	def handle_starttag(self, tag, attrs):
		if tag == "span":
			if attrs[0][0] == "class" and attrs[0][1] == "STYLE13":
				self.is_redspan = 1
			if attrs[0][0] == "class" and attrs[0][1] == "STYLE12":
				self.is_bluespan = 1

	def handle_endtag(self, tag):
		if tag == "span":
			if self.is_redspan == 1:
				self.is_redspan = ""
			if self.is_bluespan == 1:
				self.is_bluespan = ""

	def handle_data(self, data):
		if self.is_redspan == 1:
			self.balls.append(data)
		if self.is_bluespan == 1:
			self.balls.append(data)

if __name__ == "__main__":
	content = urllib.request.urlopen("http://www.3dcp.cn/zs/gonggao.php?type=ssq&year=2016").read()
	ball = MyHTMLParser()
	ball.feed(content.decode("GB2312"))
	fp = open("old2016.txt", "w")

	for i in range(0, len(ball.balls)):
		print(i, ball.balls[i])
		fp.write(str(ball.balls[i]))
		if (i + 1) % 2 == 0:
			fp.write("\n")
		##else:
		##	//fp.write(" ")

	ball.close()
