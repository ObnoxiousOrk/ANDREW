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

def calc(command):

	def add(nums):
		vTotal = nums[0]
		for num in nums[1:]:
			vTotal += num
		return vTotal

	def sub(nums):
		vTotal = nums[0]
		for num in nums[1:]:
			vTotal -= num
			print(vTotal)
		return vTotal

	def div(nums):
		vTotal = nums[0]
		for num in nums[1:]:
			vTotal /= num
		return vTotal

	def mult(nums):
		vTotal = nums[0]
		for num in nums[1:]:
			vTotal *= num
		return vTotal

	if "divided by" in command or "/" in command:
		aCommand = split(command)
		aDivNums = []

		for i in range(len(aCommand)):
			if aCommand[i:i+2] == ["divided", "by"]:
				try:
					aDivNums.append(int(aCommand[i-1]))
					aDivNums.append(int(aCommand[i+2]))

					aCommand[i + 2] = 1

				except ValueError:
					print("You can only divide numbers")
					return

			if aCommand[i] == "/":
				try:
					aDivNums.append(int(aCommand[i-1]))
					aDivNums.append(int(aCommand[i+1]))

					aCommand[i + 1] = 1

				except ValueError:
					print("You can only divide numbers")
					return

		print(aDivNums)

		return div(aDivNums)

	if "x" in command:
		aCommand = split(command)
		aTimesNums = []

		for i in range(len(aCommand)):
			if aCommand[i] == "x":

				try:
					aTimesNums.append(int(aCommand[i-1]))
					aTimesNums.append(int(aCommand[i+1]))

					aCommand[i + 1] = 1

				except ValueError:
					print("You can only multiply numbers")
					return

		print(aTimesNums)

		return mult(aTimesNums)

	if "add" in command or "+" in command:
		aCommand = split(command)
		aAddNums = []

		print(aCommand)

		for i in range(len(aCommand)):
			print(aCommand[i])
			if aCommand[i] == "add" or aCommand[i] == "+":
				print(command[i-1], command[i+1])
				try:
					aAddNums.append(int(aCommand[i-1]))
					aAddNums.append(int(aCommand[i+1]))

					aCommand[i + 1] = 0

				except ValueError:
					print("You can only add numbers")
					return

		print(aAddNums)

		return add(aAddNums)

	if "take away" in command or "subtract" in command:
		aCommand = split(command)
		aSubNums = []

		for i in range(len(aCommand)):
			if aCommand[i] == "subtract":

				try:
					aSubNums.append(int(aCommand[i-1]))
					aSubNums.append(int(aCommand[i+1]))

					aCommand[i + 1] = 0

				except ValueError:
					print("You can only take away numbers")
					return

			elif aCommand[i:i+2] == ["take", "away"]:
				try:
					aSubNums.append(int(aCommand[i-1]))
					aSubNums.append(int(aCommand[i+2]))

					aCommand[i + 2] = 0

				except ValueError:
					print("You can only take away numbers")
					return

		print(aSubNums)

		return sub(aSubNums)

	# add(1, 2, 3, 4)
	# print(sub(10, 5, 2))
	# print(div(27, 3, 3))

	# print(mult(2, 2, 2, 3))

# print(calc("what is 1 plus 1"))



"""
SEVERE ISSUES WITH MULTIPLE OPERATIONS
CANT DO BODMAS

FIND A WAY OF REMOVING NUMBERW+S WITHOUT CUCKING IT
"""
