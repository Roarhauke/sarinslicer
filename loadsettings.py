import json

if __name__ == '__main__':
	print("get outta here") # i feel like im high on sarin
	print("free cookies: https://youtu.be/dQw4w9WgXcQ") # wonder how many people i will rickroll
else:
	print("loadsettings module initializing")
	class CSettings: # define CSettings=( CodeSettings ) class
		def __init__ (self, name, volx, voly, volz, maxspeed, prefspeed): # constructer
			self.name = name
			self.volx = volx
			self.voly = voly
			self.volz = volz
			self.maxspeed = maxspeed
			self.prefspeed = prefspeed
	def loadSetFromFile(filename: str): # define LSFF function
		try:
			file = open(filename, "r") # load file
		except:
			raise Exception("requested file does not exist")
		try:
			pars = json.loads(file.read()) # parse da file
		except:
			raise Exception("json parse error")
		file.close()
		try: # prepare vals. for constructor
			name = pars["name"]
			volx = pars["volx"]
			voly = pars["voly"]
			volz = pars["volz"]
			mspeed = pars["maxspeed"]
			pspeed = pars["prefspeed"]
		except:
			raise Exception("data missing")
		setts = CSettings(name, volx, voly, volz, mspeed, pspeed) # code that might be usefull
		return setts # --::--
