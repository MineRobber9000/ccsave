import base64
from ccsave.enums import Preferences, Upgrades, Achievements
from urllib.parse import quote_plus as encode

def number(s):
	try:
		return int(s)
	except:
		try:
			return float(s)
		except:
			return 0

preferences = Preferences()

upgrades = Upgrades()

achievements = Achievements()

class Game:
#                             00000000001111111
#                             01234567890123456
	ALL_ON_PREFERENCES = "11111111001111110"
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
		self.achievements = [x=="1" for x in self.data.pop(0)]
		self.buffs = self.data.pop(0)
		del self.data
		self.preferences = [self.preferences[x]==self.ALL_ON_PREFERENCES[x] for x in range(len(self.preferences))]

	def write_save(self,level=0):
		if level==0:
			return self.write_save(1)
		elif level==3:
			print("Warning: commented save not available")
			return self.write_save(2)
		ret = ""
		ret += self.version+"|" # Game version
		ret += "|" # "//just in case we need some more stuff here"
		ret += ";".join(str(x*1000) for x in (self.session_start, self.legacy_start, self.save_tstamp))+";"+";".join((self.name, self.seed))+"|"
		ret += "".join(self.ALL_ON_PREFERENCES[x] if self.preferences[x] else toggle(self.ALL_ON_PREFERENCES[x]) for x in range(len(self.preferences)))+"|"
		ret += self.cookie_data+"|"
		ret += self.building_data+"|"
		ret += self.upgrades+"|"
		ret += " ".strip().join("1" if self.achievements[x] else "0" for x in range(achievements.v))+"|"
		ret += self.buffs
		if level==2:
			return ret
		ret = encode(base64.b64encode(ret.encode("utf-8"))+b"!END!")
