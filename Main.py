from Entry import Entry;
from collections import Counter;
import sys;

#Store list of entries
entries = []


print "Welcome to Greenphire employee Powerball entry system.."

while (True):
	
	inV = raw_input("Press 1 for a new entry, 2 to generate results, q to quit...")
	if (inV == "1"):
		#create new entry
		tmp = Entry()
		tmp.setFName(raw_input("First Name: "))
		tmp.setLName(raw_input("Last Name: "))
		
		successNum = 0
		while (successNum != 5):
			firstNum = raw_input("Enter #"+ str(successNum+1) +"  Number (1-69): ")
			if (tmp.addNum(firstNum)):
				Entry.numUsage.append(firstNum)
				successNum = successNum + 1
			else:
				print "Number must be between 1 and 69 and no duplicate numbers allowed."

		validPower = 0
		while (validPower != 1):
			power = raw_input("Powerball Num (1 - 26): ")
			if (tmp.setPower(power)):
				tmp.setPower(power)
				Entry.powerUsage.append(power)
				validPower = 1
			else:
				print "Number must be between 1 and 26"

		print "You have successfully added an entry for " + tmp.getName()
		entries.append(tmp)

	elif (inV == "2"):
		#print out results
		for e in entries:
			print e
		top5 = Counter(Entry.numUsage).most_common(5)
		print "Powerball winning numbers: " + str(top5[0][0]) + " " + str(top5[1][0]) + " " + str(top5[2][0]) + " " + str(top5[3][0]) + " " + str(top5[4][0]) + " Powerball: " + str(Counter(Entry.powerUsage).most_common(1)[0][0])
		print ""
		print "Good bye!"
		sys.exit(0)

	elif (inV == "q"):
		print "Good bye!"
		sys.exit(0)
		


