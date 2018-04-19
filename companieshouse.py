from bs4 import BeautifulSoup
import requests
import pyperclip
import webbrowser
import os

def company_details(flag):
	'''Search for address, company number'''
	c = input("\nCompany name > ")
	#need to feed query in somehow
	query = c.replace(' limited', '')
	query = query.replace(' plc', '')
	query = query.replace(' llp', '')
	query = query.replace(' ltd', '')
	record = []
	addresses = []
	companystrings = ''
	url = "https://beta.companieshouse.gov.uk/search/companies?q="+query

	data = requests.get(url)
	data = data.text
	soup = BeautifulSoup(data, "html.parser")
	for link in soup.find_all('a'):
		comp_option = str(link)
		if 'SearchSuggestions' in comp_option:
			comp_url = str(link.get('href'))
			comp_ref = comp_url.replace('/company/', '')
			namepart = str(link.contents).replace('<strong>', '').replace('</strong>', '').replace('[', '').replace(']', '').replace('\\n', '').replace(',', '').replace("'", '')
			namepart = ' '.join(namepart.split())
			nameoption = namepart.strip().lstrip()
			companystrings = nameoption
			record.append((companystrings, comp_ref))

	try:
		final_list = []
		for link in soup.find_all('p', class_=""):
			if "<strong" not in str(link) and "matches" not in str(link) and "<img" not in str(link):
				addresses.append(link.contents[0])
			information = list(zip(record, addresses))
		for i in information[0:10]:
			final_list.append("{}, {}, {}.".format(i[0][0], i[0][1], i[1]))
		for index, i in enumerate(final_list):
			print("{} - {}".format(index, i))
			
		if flag == "search":
			copy = input("Copy > ")
			try:
				copy = int(copy)
				pyperclip.copy(final_list[copy])
			except:
				return
				
		elif flag == "filings":
			filing = input("Select > ")
			try:
				filing = int(filing)
				target = final_list[filing]
			except:
				return
			company_number = target.split(',')
			filings(company_number[1])
			
		elif flag == "newcomp":
			newcomp = input("Add > ")
			try:
				newcomp = int(newcomp)
				target = final_list[newcomp]
			except:
				return
			company_deets = target.split(',')
			new_company(company_deets)

		else:
			return
			
	except:
		return "No companies found!"
	else:
		return

def filings(compnum):
	compnum = compnum.strip()
	linklist = []
	doclist = []
	datelist = []
	dates = []

	url = "https://beta.companieshouse.gov.uk/company/{}/filing-history".format(compnum)
	filingpage = requests.get(url)
	filingtext = filingpage.text
	soup = BeautifulSoup(filingtext, "html.parser")

	for link in soup.find_all('a', class_="download"):
		hyperlink = link.get('href')
		linklist.append(hyperlink)
	for doc in soup.find_all('td', class_="filing-type"):
		doccontent = doc.contents[0].strip()
		doclist.append(doccontent)
	for date in soup.find_all('td', class_="nowrap"):
		datecontent = date.contents[0]
		datelist.append(datecontent)
	for i in datelist[::2]:
		dates.append(i)
		
	results = list(zip(dates, linklist, doclist))

	for index, i in enumerate(results):
		print("{}. {} - {}".format(index, i[0].strip(), i[2]))
		
	docselect = input("Open > ")
	
	try:
		intselect = int(docselect)
		weblink = "https://beta.companieshouse.gov.uk" + str(results[intselect][1])
		webbrowser.open(weblink)
	except Exception as e:
		print(str(e))

def my_companies():
	print('')
	complist = []
	compsel = []
	for folder in os.listdir('./mycompanies'):
		complist.append(folder)
	if complist:
		for index, i in enumerate(complist):
			filenm = "./mycompanies/" + i
			files = os.listdir(filenm)
			if "info.txt" in files:
				with open(filenm + "/info.txt", "r") as compinfo:
					comptext = compinfo.read()
					compsel.append("{}".format(comptext))
					print("\n{}. {}".format(index, comptext))
			
		new = input("\nSelect, or 'N' to add new > ")
		if new.upper() == "N":
			try:
				company_details("newcomp")
			except:
				return		
		elif len(new) > 0:
			try:
				new = int(new)
				pyperclip.copy(compsel[new])
			except:
				return
		else:
			return
				
	else:
		new = input("\nNo companies, N to add new > ")
		if new.upper() == "N":
			try:
				company_details("newcomp")
			except:
				return
		else:
			return

def new_company(compnum):
	foldername = "./mycompanies/{}".format(compnum[0])
	os.mkdir(foldername)
	with open(foldername + "/info.txt", "w+") as newinfo:
		newinfo.write(compnum[0])
		newinfo.write("\n")
		newinfo.write(compnum[1].strip())
		newinfo.write("\n")
		address = ','.join(compnum[2::]).strip()
		newinfo.write(address)

def open_company():
	'''Will give ability to open page on comphouse'''
	return

