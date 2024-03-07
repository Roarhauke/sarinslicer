import json

if __name__ == '__main__':
	print("get outta here") # i feel like im high on sarin
	print("free cookies: https://youtu.be/dQw4w9WgXcQ") # wonder how many people i will rickroll
else:
	print("loadsettings module initializing")
	class CSettings: # define CSettings class
		def __init__ (self, volx, voly, volz, speed): # constructer
			self.volx = volx
			self.voly = voly
			self.volz = volz
			self.speed = speed
	def loadSetFromFile(filename: str) -> CSettings: # define LSFF function
		file = open(filename, "r") # load file
		pars = json.loads(file.read()) # parse da file
		setts = CSettings() # code that might be usefull
		return setts # --::--
