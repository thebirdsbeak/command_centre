from random import randint
import webbrowser
import csv
import requests
from bs4 import BeautifulSoup

def grab_legislation():
    '''Main search handler'''
    url = "http://www.legislation.gov.uk"
    search = input("Title\n>>> ")
    year = input("Year\n>>> ")
    if year:
        url = url + "/id?title={}&year={}".format(search, year)
    else:
        url = url + "/id?title={}".format(search)
    page_data = requests.get(url)
    if page_data.status_code == 300:
        handle_300(page_data)
    elif page_data.status_code == 200:
        handle_200(page_data, url, True)


def handle_300(page_data):
    result_list = []
    base_url = "http://www.legislation.gov.uk"
    page_text = page_data.text
    soup = BeautifulSoup(page_text, "html.parser")
    for link in soup.find_all("a"):
        if "/id/" in link.get('href'):
            result_list.append([link.get('href'), link.contents[0]])
    for index, document in enumerate(result_list):
        print("{}. {}".format(index, document[1]))
    selected_document = input("\n>>> ")
    try:
        document_index = int(selected_document)
    except ValueError:
        print("value error - please use numbers")
    final_url = base_url + result_list[document_index][0]
    handle_200(page_data, final_url, False)


def handle_200(page_data, url, flag):
    if flag == False:
        url = url.replace("/id/", "/")
        url += "/contents?view=plain"
    elif flag == True:
        url = page_data.headers['Content-Location'].replace("/data.htm", "")
        url += "?view=plain" 
    else:
        return
    webbrowser.open(url)


#def search_legislation(page_data, url):
#    crossheadings = []
#    sections = []
#    schedules = []
#    contents_page = requests.get(url)
#    contents_text = contents_page.text
#    soup = BeautifulSoup(contents_text, "html.parser")
#    for i in soup.find_all("a"):
#        elif "/crossheading/" in i.get('href'):
#            if i.get('href' not in str(crossheadings):
#                crossheadings.append([i.contents, i.get('href')])
#        elif "/section/" in i.get('href'):
#            if i.get('href') not in str(sections):
#                sections.append([i.contents, i.get('href')])
#        elif "/schedule" in i.get('href'):
#            schedules.append(i.get('href'))
#    print("\nHeadings: {}\nSections: {}\nSchedules: {}\n".format(len(crossheadings), len(sections), len(schedules)))

    
#def build_extract():
#    return

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
        result_string = ""
        for line in gdpr:
            if searchword in line[0]:
                print("Chapter {}\n{}\n{}\n{}({})\n{}\n".format(line[5], line[4], line[3], line[2], line[1], line[0]))
                result_string += "Chapter {}\n{}\n{}\n{}({})\n{}\n\n".format(line[5], line[4], line[3], line[2], line[1], line[0])
        if len(result_string) > 0:
            open_choice = input("Save report? (y/n)\n>>> ")
            if open_choice.upper() == "Y":
                with open("assets/report.txt", "w") as search_file:
                    search_file.write(result_string)
                webbrowser.open("assets/report.txt")
    else:
        for line in gdpr:
            if str(searchword) == str(line[2]):
                print("Chapter {}\n {}\n{}\n{}({})\n{}\n".format(line[5], line[4], line[3], line[2], line[1], line[0]))
   
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
