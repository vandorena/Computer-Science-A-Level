import re
import requests


#need to add a run for the regex url list maker

#with open("C:\Users\Alex\Documents\Work\A Levels 6th Form\Computer Science\Regex Bruteforce URL list creator.py") as urllistmaker:
#    exec(urllistmaker.read())


# the regex command i made didn't work that well, and so i grabbed one off the internet.

def urlcheck(url):
    urlformat = re.compile(r'(https:\/\/www\.|http:\/\/www\.|https:\/\/|http:\/\/)?[a-zA-Z]{2,}(\.[a-zA-Z]{2,})(\.[a-zA-Z]{2,})?\/[a-zA-Z0-9]{2,}|((https:\/\/www\.|http:\/\/www\.|https:\/\/|http:\/\/)?[a-zA-Z]{2,}(\.[a-zA-Z]{2,})(\.[a-zA-Z]{2,})?)|(https:\/\/www\.|http:\/\/www\.|https:\/\/|http:\/\/)?[a-zA-Z0-9]{2,}\.[a-zA-Z0-9]{2,}\.[a-zA-Z0-9]{2,}(\.[a-zA-Z0-9]{2,})?') 
    url = urlformat.search(url)
    return bool(url)
def onlinecheck(url):
    status = "Offline"
    httpsrequest = requests.head(url)
    if httpsrequest.status_code == 200:
        status = "Online"
    elif httpsrequest.status_code == 404:
        status = "Offline"
    else:
        status = "Unkown"
        
url = input("Input your suggested url here: ")
print(f"Your url is a {urlcheck(url)} url")
endoffile = False
urlfile = open('URLlist.txt', 'r')
while endoffile == False:
    urlline = urlfile.readline()
    if not urlline:
        break
    thisurlonline = onlinecheck(urlline)
    if thisurlonline == True:
        print(f"{urlline} is a {urlcheck(urlline)} url and it's status is {onlinecheck(urlline)} " )
