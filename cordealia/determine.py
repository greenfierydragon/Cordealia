class Determine:
	def __init__(self):
		self.ask = ""
		self.f1=""
		self.f2 =""
		self.f3 = ""
		self.c = 9
	def respond(self, ask):
		self.ask = ask
		self.ask += " "
		if self.ask.startswith("how many"):
			self.c=9
			
			l=""
			while self.ask[self.c] != " ":
				l += self.ask[self.c]
				self.c+=1
					
			self.f1 = l
			l= ""
			self.c+=4
			while self.ask[self.c] != " ":
				l += self.ask[self.c]
				self.c+=1
			self.f3 = l
			l= ""
			self.c+=1
			while self.ask[self.c] != " ":
				l += self.ask[self.c]
				self.c+=1
			self.f2=l
			
		return ([self.f1, self.f2, self.f3])
