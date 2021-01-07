from time import sleep
from termcolor import cprint as cpr
import platform
import sys
import os
from utils import clear
import output
from future import print as pr
debug = True
noDebug = False
def compile(filepath, out, dbg, compileType):
	error = ErrorHandler(dbg)
	shouldWrite = True
	FileData = ["from time import sleep", "from termcolor import cprint as cpr", "import sys", "import varHandlerSystem", "from utils import clear" , "varHandler = varHandlerSystem.variableHandler()"]
	CompiledFile = ""
	f = open(filepath)
	count = len(f.readlines())
	cpr("Compiling " + str(count) + " lines...", "yellow")
	f.close()
	f = open(filepath)
	numDone = 0
	sleep(0.5)
	for line in f:
		clear()
		cpr(str(numDone) + " / " + str(count), "blue")

		if line.startswith("out "):
			toPrint = line.split("out ")[1]
			FileData.append("print('"+toPrint.replace("\n", "")+"')")

		elif line.startswith("outvar "):
			varToPrint = line.split("outvar ")[1]
			FileData.append("print(str(varHandler.get('"+varToPrint.replace("\n", "")+"')))")



		elif line == "exit":
			FileData.append("sys.exit()")
		elif line == "clear":
			FileData.append("clear()")


		elif line.startswith("delay "):
			try:
				float(line.split("delay ")[1])
			except ValueError:
				error.BuildDelayStringError()
				shouldWrite = False
				break			
			DelayToDo = line.split("delay ")[1]
			FileData.append("try:")
			FileData.append("	sleep(float("+DelayToDo.replace("\n", "")+"))")
			FileData.append("except ValueError:")
			FileData.append("	sys.exit()")

		elif line.startswith("-grey out "):
			toPrint = line.split("-grey out ")[1]
			FileData.append("cpr('"+toPrint.replace("\n", "")+"', 'grey')")

		elif line.startswith("-red out "):
			toPrint = line.split("-red out ")[1]
			FileData.append("cpr('"+toPrint.replace("\n", "")+"', 'red')")

		elif line.startswith("-green out "):
			toPrint = line.split("-green out ")[1]
			FileData.append("cpr('"+toPrint.replace("\n", "")+"', 'green')")

		elif line.startswith("-yellow out "):
			toPrint = line.split("-yellow out ")[1]
			FileData.append("cpr('"+toPrint.replace("\n", "")+"', 'yellow')")

		elif line.startswith("-blue out "):
			toPrint = line.split("-blue out ")[1]
			FileData.append("cpr('"+toPrint.replace("\n", "")+"', 'blue')")

		elif line.startswith("-magenta out "):
			toPrint = line.split("-magenta out ")[1]
			FileData.append("cpr('"+toPrint.replace("\n", "")+"', 'magenta')")

		elif line.startswith("-cyan out "):
			toPrint = line.split("-cyan out ")[1]
			FileData.append("cpr('"+toPrint.replace("\n", "")+"', 'cyan')")	

		elif line.startswith("-white out "):
			toPrint = line.split("-white out ")[1]
			FileData.append("cpr('"+toPrint.replace("\n", "")+"', 'white')")

		elif line.startswith("-"):
			error.BuildPreStringParam()
			shouldWrite = False
			break

		elif line.startswith("var"):
			partList1 = line.split("=")
			varName = partList1[0].split("var ")[1].strip()
			varVal = partList1[1].strip()
			FileData.append("varHandler.create(\""+varName+"\", \""+varVal+"\")")

		elif line.startswith("~"):
			pass

		else:
			error.SyntaxError()

		numDone = numDone + 1




	if shouldWrite:
		outFile = open(out, "w")
		for compiledLine in FileData:
			CompiledFile = CompiledFile + compiledLine + "\n"
		outFile.write(CompiledFile)
		outFile.close()
		cpr("Wrote python file!", "green")
		if compileType:
			os.system("python " + out)
		else:
			cpr("Plain run execution is currently not supported, sorry!", "red")
			


class ErrorHandler():
	def __init__(self, dbg):
		if dbg:
			cpr("Initialized Debug Error Evals", "green")
			self.dbg = True
		else:
			self.dbg = False
	def BuildPreStringParam(self):
		if not self.dbg:
			cpr("ERROR - BuildPreStringParam", "red")
		else:
			cpr("ERROR - BuildPreStringParam\nDebugVal: PreString Parameter may not support your input string,\nor you may have mispelled a supported parameter", "red")
	def SyntaxError(self):
		if not self.dbg:
			cpr("ERROR - SyntaxError", "red")
		else:
			cpr("ERROR - SyntaxError\nDebugVal: You have a syntax error in your code. Maybe you forgot to use the proper statement?", "red")
	def BuildDelayStringError(self):
		if not self.dbg:
			cpr("ERROR - Delay Parameters cannot be of type STRING.", "red")
		else:
			cpr("ERROR - Delay Parameters cannot be of type STRING.\nDebugVal: You may have accidentally entered a string.", "red")
		


if __name__ == '__main__':
	compile("in.mth", "out.py", debug, output.py)