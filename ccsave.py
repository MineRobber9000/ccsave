import enum,base64

def number(s):
	try:
		return int(s)
	except:
		try:
			return float(s)
		except:
			return 0

class Settings(enum.Enum):
	def __init__(self):
		super(Settings, self).__init__(self)

class Upgrades(enum.Enum):
	pass

class Achievements(enum.Enum):
	pass

class Game:
	def __init__(self,save="",savefile=""):
		if savefile and not save:
			with open(savefile) as f:
				save = f.read().strip()
		elif not (savefile or save):
			raise Exception("Either pass in a save or a save file!")
		self.data = base64.b64decode(save).decode("utf-8").split("|")
		self.version = self.data.pop(0)
		self.reserved = self.data.pop(0)
		startdata = self.data.pop(0).split(";")
		self.session_start, self.legacy_start, self.save_tstamp = (int(x)/1000 for x in [startdata.pop(0) for y in range(3)])
		self.name = startdata.pop(0)
		self.seed = startdata.pop(0)
		self.preferences = self.data.pop(0)
		self.cookie_data = self.data.pop(0)
		self.building_data = self.data.pop(0)
		self.upgrades = self.data.pop(0)
		self.achievements = self.data.pop(0)
		del self.data
