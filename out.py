from time import sleep
from termcolor import cprint as cpr
import sys
import varHandlerSystem
varHandler = varHandlerSystem.variableHandler()
varHandler.create("test", "test1")
varHandler.create("test", "test2")
print(varHandler.get('test'))
try:
	sleep(float(25))
except ValueError:
	sys.exit()
