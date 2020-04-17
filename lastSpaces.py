def deleteSpaces(hola):
	newHola = ""
	flag = False
	for char in hola:
		if flag:
			if char == " ":
				return newHola
			else:
				newHola = newHola + char
				flag = False
		else:
			if char == " ":
				newHola = newHola + char
				flag = True
			else:
				newHola = newHola + char
def main():
	hola = "hola hola              "
	print(deleteSpaces(hola))
if __name__ == '__main__':
	main()
