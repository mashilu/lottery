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
		self.is_serialspan = ""
		self.balls = []

	def handle_starttag(self, tag, attrs):
		if tag == "span":
			if attrs[0][0] == "class" and attrs[0][1] == "STYLE13":
				self.is_redspan = 1
			if attrs[0][0] == "class" and attrs[0][1] == "STYLE12":
				self.is_bluespan = 1
			if attrs[0][0] == "class" and attrs[0][1] == "end":
				self.is_serialspan = 1

	def handle_endtag(self, tag):
		if tag == "span":
			if self.is_redspan == 1:
				self.is_redspan = ""
			if self.is_bluespan == 1:
				self.is_bluespan = ""
			if self.is_serialspan == 1:
				self.is_serialspan = ""

	def handle_data(self, data):
		if self.is_serialspan == 1:
			self.balls.append(data)
		if self.is_redspan == 1 or self.is_bluespan == 1:
			for a_ball in data.split():
				self.balls.append(a_ball)

if __name__ == "__main__":
	fp = open("his_dlt.txt", "w")
	base_url = "http://www.3dcp.cn/zs/gonggao.php?type=dlt&year="

	for url in [base_url + str(x) for x in range(2007, 2017, 1)]:
		content = urllib.request.urlopen(url).read()
		ball = MyHTMLParser()
		ball.feed(content.decode("GB2312"))
		for i in range(0, len(ball.balls)):
			fp.write(str(ball.balls[i]))
			if (i + 1) % 8 == 0:
				fp.write("\n")
			else:
				fp.write(" ")

	fp.close()
	ball.close()
