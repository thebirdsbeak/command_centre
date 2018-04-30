#!/usr/bin/env python3

'''
Command line program for day to day tasks
'''

# Feature ideas:
# - Search GDPR
# - make Notepad save old tasks

from companieshouse import company_details, my_companies
from notepad import to_do, help_function
from fun import wiki, headlines, list_crypto, select_coins
from fun import definition, synonym, quicksearch
from legalfunctions import maxims, search_gdpr, open_gdpr, grab_legislation, clauses


def startup():
        '''Main loop input handler'''
        while True:
            print("\n1. Corporate")
            print("2. Todo")
            print("3. Legal")
            print("4. Fun")
            print("5. Help")
            inputprompt = "\n>>> "
            choice = input(inputprompt).upper()
            if choice == "1":
                print("\n1. Company details")
                print("2. Filings", )
                print("3. My Companies", )
                choicetwo = input(inputprompt).upper()
                if choicetwo == "1":
                    company_details("search")
                elif choicetwo == "2":
                    company_details("filings")
                elif choicetwo == "3":
                    my_companies()
            elif choice == "2":
                    to_do()
            elif choice == "3":
                print("\n1. Search GDPR")
                print("2. Open GDPR")
                print("3. Legislation")
                print("4. Clauses")
                print("5. Maxims")
                choicetwo = input(inputprompt).upper()
                if choicetwo == "1":
                    search_gdpr()
                elif choicetwo == "2":
                    open_gdpr()
                elif choicetwo == "3":
                    grab_legislation()
                elif choicetwo == "4":
                    clauses()
                elif choicetwo == "5":
                    maxims()
            elif choice == "4":
                print("\n1. BBC Headlines")
                print("2. Cryto prices")
                print("3. Search cryto")
                choicetwo = input(inputprompt).upper()
                if choicetwo == "1":
                    headlines()
                elif choicetwo == "2":
                    list_crypto()
                elif choicetwo == "3":
                    select_coins()
            elif choice == "5":
                help_function()
            elif choice == "Q":
                quit()
            elif choice == "":
                pass
            elif choice[0] == '/':
                quicksearch(choice.lower())
            elif choice[-1] == ';':
                definition(choice)
            elif choice[-1] == ':':
                synonym(choice)
            elif len(choice) > 3:
                if choice[0:4] == "WIKI":
                    wiki(choice.lower())
                else:
                    print("\nShaddap\n")

startup()
