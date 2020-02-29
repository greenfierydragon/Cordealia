class Stuff:
	def __init__(self):
		#weight
		self.mg = 0.1
		self.g = 1
		self.kg = 1000
		self.mt = 1000000
		self.dwt = 1.55517
		self.oz = 28.3495
		self.lbs = 453.592
		self.st = 6350.29
		self.it = 907185
		self.ms1 = 1
		self.ms2 = 1
		self.weights = ["microgram", "milligram", "gram", "kilogram", "tonne", "pennyweight", "ounce", "pound", "stone", "ton","micrograms", "milligrams", "grams", "kilograms", "tonnes", "pennyweights", "ounces", "pounds", "stones", "tons","mcg", "mg", "g", "kg", "t", "dwt", "oz", "lbs", "st", "t"]
		self.weightvalue = [0.000001, 0.001,1, 1000, 1000000,1.55517,28.3495,435.592,6350.29,907185]
	def Ask(self, mes1, mes2, amount):
		self.ms1 = 1
		if mes1 in self.weights:
			k = self.weights.index(mes1)
			self.ms1 = self.weightvalue[k % len(self.weightvalue)]
		else:
			self.ms1 = 1
		
		self.ms2 = 1
		if mes2 in self.weights:
			k = self.weights.index(mes2)
			self.ms2 = self.weightvalue[k % len(self.weightvalue)]
		else:
			self.ms2 = 1
		return((self.ms1/self.ms2)*amount)

