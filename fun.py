import requests
from bs4 import BeautifulSoup
import webbrowser
import wikipedia
import json
from fuzzywuzzy import fuzz
import wikipedia

def headlines():
	'''Gets BBC headlines'''
	print()
	data = requests.get("http://www.bbc.co.uk/news/popular/read")
	data = data.text
	soup = BeautifulSoup(data, "html.parser")
	urlist = []
	headlineslist = []
	num = 1
	for link in soup.find_all(class_="most-popular-list-item__link"):
		url = link.get('href')
		urlist.append(url)
	print('')
	for link in soup.find_all('span', class_="most-popular-list-item__headline"):
		headline = link.contents[0]
		print('{}. {}'.format(str(num), headline))
		headlineslist.append(headline)
		num += 1
	print('')
	results = list(zip(urlist, headlineslist))
	index = (input("\nSelect headlines >>> "))
	if len(index) > 0:
		selections = index.split(',')
		for i in selections:
			i = int(i)
			i -= 1
			open_article = results[i]
			webbrowser.open("http://www.bbc.co.uk"+open_article[0])
		input("")
	else:
		return

def definition(search):
	'''When ';' at end of input, print definitions'''
	url = "http://www.dictionary.com/browse/{}?s=t"
	search = search.replace(";","").replace(" ","")
	endpoint = url.format(search)
	searchcontent = requests.get(endpoint)
	data = searchcontent.text
	soup = BeautifulSoup(data, "html.parser")
	print('')
	for i in soup.find_all(class_="def-content"):
		i = i.text
		i = i.lstrip()
		i = " ".join(i.split())
		print(i)
		print("")
	input("")
	
def synonym(search):
	'''When ':' at end of input, print synonyms'''
	url = "http://thesaurus.com/browse/{}?s=t"
	search = search.replace(":","").replace(" ","")
	endpoint = url.format(search)
	searchcontent = requests.get(endpoint)
	data = searchcontent.text
	soup = BeautifulSoup(data, "html.parser")
	print('')
	for i in soup.find_all(class_="text"):
		i = i.text
		i = i.lstrip()
		i = " ".join(i.split())
		print(i)
	input("")
   
def quicksearch(query):
	'''Runs a quick search on main loop'''
	duck = "https://duckduckgo.com/?q="
	query = query.replace("/", "+")
	search = duck+query
	webbrowser.open(search)
	input("")


def list_crypto():
	r = requests.get('https://api.coinmarketcap.com/v1/ticker/')
	data = r.json()
	for i in data:
		if float(i['percent_change_1h']) > 1:
			print('{} ({}) - {} ({})'.format(i['name'], i['symbol'], i['price_usd'], i['percent_change_1h']))
		elif float(i['percent_change_1h']) < -1:
			print('{} ({}) - {} ({})'.format(i['name'], i['symbol'], i['price_usd'], i['percent_change_1h']))
		else:
			print('{} ({}) - {} ({})'.format(i['name'], i['symbol'], i['price_usd'], i['percent_change_1h']))


def select_coins():
	r = requests.get('https://api.coinmarketcap.com/v1/ticker/')
	data = r.json()
	selection = input('Currency > ')
	if selection:
		print('')
		for i in data:
			if fuzz.ratio(selection, i['name']) > 65:
				print("{} ({}) - {} ({})".format(i['name'],  i['symbol'], i['price_usd'], i['percent_change_1h']))
	else:
		return

def wiki(choice):
    '''bring back a snippet from wikipedia'''
    wikisearch = choice[4::].strip()
    print(wikisearch)
    if len(wikisearch) > 0:
        try:
            summary = wikipedia.summary(wikisearch)
        except:
            summary = "No summary found! \n\n(╯°□°）╯︵ ┻━┻"
        print('')
        print(summary.replace("\n", "\n\n"))
    else:
        return
