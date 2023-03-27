import configparser

class getconfig(object):

	def __init__(self):
		self.configs = configparser.ConfigParser()
		self.configs.read('config.ini')

	def conf(self):
		#print(self.configs)
		return self.configs["Default"]

	def update_count(self, newcount):
		self.configs["Default"]["TRANSCRIPT_COUNT"] = newcount
		with open('config.ini','w') as configfile:
			self.configs.write(configfile)
			
