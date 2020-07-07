import listener as l
from say import say
from calculator import calc

from count import count

class INTERPRET():
	def __init__(self, command):
		self.vCommand = command

	def interpret(self):
		if "goodbye" == self.vCommand or "bye" == self.vCommand:
			exit()

		elif "count" in self.vCommand:
			say(count(self.vCommand))

		elif "what is" in self.vCommand or "what's" in self.vCommand:
			say(calc(self.vCommand))

while True:
	l.ANDREW.main()
	INTERPRETER = INTERPRET(l.vCommand)
	INTERPRETER.interpret()