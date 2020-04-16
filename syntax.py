def check(filepath):
	with open(str(filepath)) as fp:
		line = fp.readline()
		lines = []
		lines.append("{}".format(line.strip()))
		line = fp.readline()
		i = 0
		count = len(open(filepath).readlines(  ))
		while True:
			if lines[i].startswith("out "):
				valToPrint = lines[i].split("out ",1)[1]
				print(valToPrint)
				i=i+1
				if i == count:
					break
			elif lines[i].startswith("getUser "):
				valToInput = lines[i].split("getUser ", 1)[1]
				input(valToInput)
				i=i+1
				if i == count:
					break