import convert, determine

determine = determine.Determine()
stuff = convert.Stuff()
while True :
	ask = input("What do you need to know? ")
	
	ask = ask.lower()
	determineresult = determine.respond(ask)
	
	a = stuff.Ask(determineresult[1], determineresult[0], float(determineresult[2]))
	print(a)
