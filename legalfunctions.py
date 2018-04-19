from random import randint
import webbrowser
import csv

def search_gdpr():
	'''Dispatches GDPR search'''
	choicethree = input("\nSearch by word or [number]\n\n>>> ")
	if len(choicethree) > 0:
		if choicethree[0] == "[":
			article = choicethree.replace("[", "").replace("]", "").strip()
			try:
				article = int(article)
				return_search(article)
			except ValueError:
				print("\nOnly put numbers in the article search!")
		else:
			return_search(choicethree)
			
def return_search(searchword):
	'''Returns GDPR search'''
	gdpr = []
	with open("assets/gdpr.csv") as legislation:
		articlelist = csv.reader(legislation)
		for row in articlelist:
			gdpr.append(row)
			
	if type(searchword) == str:
		for line in gdpr:
			if searchword in line[0]:
				print(line)
		
	else:
		for line in gdpr:
			if str(searchword) == line[2]:
				print(line)
		
	
def open_gdpr():
	webbrowser.open("assets/gdpr.html")

def maxims():
    '''Reads the maxims and passes the variable to function
    according to input'''
    contentslist = []
    maximlist = open("assets/maxims.txt", "r")
    maximlines = maximlist.readlines()
    maximlist.close()
    for index, i in enumerate(maximlines):
        contentslist.append((index,i))	

    def randomaxim(contentslist):
        '''prints a random maxim'''
        maximselection = randint(0, len(contentslist))
        print("{} - {}".format(contentslist[maximselection][0], contentslist[maximselection][1]))
        input("")

    def searchmaxim(contentslist, maximsearch):
        '''When word input, searches maxim for word and prints hits'''
        foundlist = []
        print()
        for i in contentslist:
            text = i[1]
            if str(maximsearch) in text:
                textindex = i[0]
                selectedtext = i[1]
                print("{} - {}".format(textindex, selectedtext))
                foundlist.append(textindex)
        if len(foundlist) == 0:
            print("Could not find '{}'".format(maximsearch))
            print("\n(╯°□°）╯︵ ┻━┻")

        input("")
				
    def maximindex(contentslist, maximsearch):
        '''Grabs a maxim by numerical index'''
        try:
            integer = int(maximsearch.replace("/",""))

            try:
                indexedtext = contentslist[integer]
                print("{} - {}".format(indexedtext[0], indexedtext[1]))

            except Exception:
                print("Search index is not in range {}".format(len(contentslist)))
                print("\n(╯°□°）╯︵ ┻━┻")

        except Exception as e:	
            print("/ = textsearch, // = index search")
        input("")
		
    maximsearch = input("\nMaxim >>> ")	
    if maximsearch == "":
        randomaxim(contentslist)
    if len(maximsearch) > 1:
        if maximsearch[0] == "/":
            maximindex(contentslist, maximsearch)
        else:
            searchmaxim(contentslist, maximsearch)
