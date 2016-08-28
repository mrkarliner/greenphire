import sys

class Entry:


	numUsage = []
	powerUsage = []

	def __init__(self):
		self.fName = ""
		self.lName = ""
		self.nums = [];
		self.power = ""
		self.availableNums = range(1,70)
		

	def setFName(self, fName):
		self.fName = fName
	
	def setLName(self, lName):
		self.lName = lName

	def setPower(self, power):
		p = int(power);
		if (p >= 0 and p <= 26):
			self.power = p
			return True
		else:
			return False

	def addNum(self, num):
		num = int(num)	
		if (num in self.availableNums and (num >= 0 and num <= 69)):
			self.nums.append(num)
			self.availableNums[num - 1] = sys.maxsize
			return True
		else:
			return False

	def getName(self):
		return self.fName + " "+ self.lName

	def getNums(self):
		return self.nums

	def __str__(self):
		num = " ".join(str(n) for n  in self.nums)
		return self.fName +  "  " + self.lName + " " +  num  + " Powerball " + str(self.power)

	def __rpr__(self):
		return str(self.__str__())

