from say import say

##--[count every _____ from ___ to ___]--##

def count(command):
	vJump = 0

	vStartIndex = command.find("from") + 5
	vSpaceAfterStart = command.find(" ", vStartIndex)

	vEndIndex = command.find("to") + 3
	vSpaceAfterEnd = command.find(" ", vEndIndex)

	vJumpIndex = command.find("every") + 6
	vSpaceAfterJump = command.find(" ", vJumpIndex)

	if vStartIndex == -1 or vEndIndex == -1:
		print("No start/end specified")

	if vJumpIndex == -1 + 6:
		vJump = 1

	elif vSpaceAfterJump == -1:
		vSpaceAfterJump = len(command)

	if vSpaceAfterStart == -1:
		vSpaceAfterStart = len(command)

	if vSpaceAfterEnd == -1:
		vSpaceAfterEnd = len(command)

	# print(vJumpIndex)

	try:
		vStart = int(command[vStartIndex:vSpaceAfterStart])
		vEnd = int(command[vEndIndex:vSpaceAfterEnd])
		if vJump != 1:
			vJump = int(command[vJumpIndex:vSpaceAfterJump])

	except ValueError:
		print("Invalid Input, use only numbers")
		say("Invalid Input, use only numbers")
		return

	print(vStart, vEnd)

	if vStart > vEnd:
		vEnd -= 1
		vJump = -1
	else:
		vEnd += 1

	print(vJump)


	vCount = ""
	for i in range(vStart, vEnd, vJump):
		vCount += str(i) + " "

	return vCount