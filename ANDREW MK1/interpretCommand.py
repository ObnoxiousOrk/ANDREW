##--Interprets Commands and handles telling other programs what to do based off of them--#
import listener as l
import say

import count
import calculate as calc
l.ANDREW.main()

class COMMAND():
	def __init__(self, command):
		self.aCommand = command

		"""
		Each command should be represented by a 4 digit number where each digit tells something about the command

		DIGIT - WHAT IT MEANS
		1 - The unique number "main command" identifier
		2 - The "sub-command" - top level commands have this as 0 and it sould count in the order that the command is expected to appear
		3 - If the command expects an additional value - none is 0, numeric is 1, text is 2
		"""
		self.dCommands = {"count" : '0001',
											"in" : '0111',
											"from" : '0121',
											"to" : '0131',

											"what's" : '0102',
											"add" : '0112',
											"subtract" : '0122',
											"times" : '0132',
											"divided" : '0142'}

	def codify(self):
		print(self.aCommand)

		aCommandValue = []
		aToBePopped = []

		for i in range(len(self.aCommand)):
			try:
				aCommandValueTemp = [self.dCommands[self.aCommand[i]]]
				vFoundKeyword = i
			except KeyError:
				try:
					if i - 1 == vFoundKeyword:
						aCommandValueTemp.append(int(self.aCommand[i]))
						aToBePopped.append(i)
				except TypeError:
					print("Command not found")

			aCommandValue.append(aCommandValueTemp)

		for i in range(len(aToBePopped)-1, -1, -1):
			aCommandValue.pop(aToBePopped[i])

		return aCommandValue

	def interpret(self, commandValues):
		for command in commandValues:
			if command[0] == '0001':
				vSay = count.count(commandValues)

			elif command[0] == '0102':
				vSay = calc.calc(commandValues)

		return vSay

	def main(self):
		aValues = self.codify()
		global vSay
		vSay = self.interpret(aValues)
		say.say(vSay)



HANDELER = COMMAND(l.aCommand)
HANDELER.main()