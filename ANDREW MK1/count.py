def count(commandValues):
	print(commandValues)
	for command in commandValues:
		if command[0] == '0111':
			vJump = command[1]

		elif command[0] == '0121':
			vStart = command[1]

		elif command[0] == '0131':
			vEnd = command[1]

	vCount = ""

	print(vStart, vEnd, vJump)

	if vStart <= vEnd:
		for i in range(vStart, vEnd+1, vJump):
			vCount += str(i) + " "

	else:
		for i in range(vStart, vEnd-1, vJump):
			vCount += str(i) + " "

	print(vCount)
	return vCount

# print(count([['0001'], ['0111', 1], ['0121', 1], ['0131', 10]]))
