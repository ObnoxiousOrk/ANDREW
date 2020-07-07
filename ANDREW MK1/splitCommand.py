def split(command):
	aSpaceIndex = [0]
	aCommand = []


	for char in range(len(command)):
		if command[char] == " ":
			aSpaceIndex.append(char)

		else:
			pass

	aSpaceIndex.append(len(command))

	for space in range(len(aSpaceIndex)):
		try:
			if space == 0:
				aCommand.append(command[aSpaceIndex[0]:aSpaceIndex[1]])
			else:
				aCommand.append(command[aSpaceIndex[0] + 1:aSpaceIndex[1]])
		except IndexError:
			break

		aSpaceIndex.pop(0)

	return aCommand