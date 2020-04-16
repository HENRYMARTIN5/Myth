import utils, syntax
from time import sleep
class MythCompiler:
	def __init__(self, filetype):
		print("Initializing Myth Compiler...")
		if filetype=="python":
			print("Hey! Don't try using Python here!!! Myth may have been written in Python, but you can't run Python from Myth. Or can you...")
		elif filetype=="standard/.mth":
			print("Loading compiler for FileType \".MTH Myth source file\"")
			sleep(1)
	def Run(self, filename):
		try:
			self.fp = open(filename, 'r')
		except:
			print("An error occured while parsing the file. Maybe your file path is wrong?")
		print("Running program...")
		sleep(0.5)
		utils.clear()
		syntax.check("tests.mth")
		
