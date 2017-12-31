"""
Separate out jenkins pipelines
console log files
"""

file = ""
log = open(file, "r")

api = open("api-"+file, "w")
inte = open("inte-"+file, "w")
unit = open("unit-"+file, "w")
e2e = open("e2e-"+file, "w")
other = open("other-"+file, "w")

while True:
	line = log.readline()
	if line == "":
		break # we are done
	elif line[:2] == "[a":
		api.writeline(line)
	elif line[:2] == "[i":
		inte.writeline(line)
	elif line[:2] == "[u":
		unit.writeline(line)
	elif line[:2] == "[e":
		e2e.writeline(line)
	else:
		other.writeline(line)

log.close()
api.close()
inte.close()
unit.close()
e2e.close()
other.close()
