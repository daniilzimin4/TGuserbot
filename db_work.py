import sqlite3

class Database:
	def __init__(self):
		self.connection = sqlite3.connect("status.db", check_same_thread=False)


	#AFK?
	def get_my_afk(self):
		cursor = self.connection.cursor()
		request = "SELECT status FROM statuses"
		result = cursor.execute(request).fetchone()
		return result[0]

	def set_my_afk(self, value):
		cursor = self.connection.cursor()
		request = "UPDATE statuses SET status=?"
		cursor.execute(request, (value,))
		self.connection.commit()


	#ReasonAFK
	def get_reason(self):
		cursor = self.connection.cursor()
		request = "SELECT reason FROM statuses"
		result = cursor.execute(request).fetchone()
		return result[0]

	def set_reason(self, value):
		cursor = self.connection.cursor()
		request = "UPDATE statuses SET reason=?"
		cursor.execute(request, (value,))
		self.connection.commit()


	#TimeInAFK
	def get_time_afk(self):
		cursor = self.connection.cursor()
		request = "SELECT timeAfk FROM statuses"
		result = cursor.execute(request).fetchone()
		return result[0]

	def set_time_afk(self, value):
		cursor = self.connection.cursor()
		request = "UPDATE statuses SET timeAfk=?"
		cursor.execute(request, (value,))
		self.connection.commit()
	
	