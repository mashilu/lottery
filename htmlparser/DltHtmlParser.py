from html.parser import HTMLParser


class DltHTMLParser(HTMLParser):
	def error(self, message):
		pass

	def __init__(self):
		HTMLParser.__init__(self)
		self.is_redspan = ""
		self.is_bluespan = ""
		self.is_serialspan = ""
		self.cur_result = []
		self.result = []

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
			self.cur_result.append(data.strip())
		if self.is_redspan == 1:
			for a_ball in sorted(data.strip().split()):
				self.cur_result.append(a_ball)
		if self.is_bluespan == 1:
			for a_ball in sorted(data.strip().split()):
				self.cur_result.append(a_ball)
			self.result.append(self.cur_result)
			self.cur_result = []
