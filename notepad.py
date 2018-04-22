import os

def to_do():

	def todolist():
		print("\n------------------------\n")
		todo = open("./assets/todo.txt", "r")
		lines = todo.readlines()
		for index, i in enumerate(lines):
			print("{} - {}".format(index, i))
		print("------------------------")
		   
		content = [l for l in lines]
		inputprompt = "\n>>> "
		choice = input(inputprompt).upper()
		if len(choice) > 0:
			try:
				choice = int(choice)
			except:
				return
			if choice > (len(content)-1):
				newline = input("\n{} - ".format(len(content)))
				content.append(newline + '\n')
					
			else:
				print("\n{} - {}".format(choice, content[choice]))
				with open("assets/rubbish.txt", "a") as wastebin:
					wastebin.write("\n{} - {}".format(choice, content[choice]))
				newline = input("{} - ".format(choice))
				content[choice] = newline + '\n'

			todo.close()
			writelist(content)
		else:
			todo.close()
			return

	def writelist(content):
		todowrite = open("./assets/todo.txt", "w")
		for i in content:
			if len(i) > 2:
				todowrite.write(i)
		todowrite.close()
		todolist()
	
	todolist()

def help_function():
	print('''
	Select by inserting the relevant number.
	Search for definitions by adding semicolon, e.g. bananas;
	Search for synonyms by adding colon, e.g. bananas:
	Do a quick web search with a preceding slash e.g. /bananas''')
