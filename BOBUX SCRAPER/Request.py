import requests as REQ
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import json
import ast
import re
#get YOutube URL
#Json File
#file = open("Video.json")
#data = json.load(file)
#Reads Json and outputs a dictionary
with open("Video.json", "r") as write_file:
    x = write_file.readlines()[0]
    x = ast.literal_eval(x)
print(x['URL'])
#Data
Embed = "https://www.youtube.com/watch?v=tjQIO1rqTBE"
URL = x['URL']

Session = HTMLSession()
Response = Session.get(URL)

#Parse
Soup = BeautifulSoup(Response.html.html, "html.parser")

#YT embed vid
print(Soup.find_all("meta")[18])
filt = re.search("(\"https.* )", str(Soup.find_all("meta")[18]))
print(filt[1])
Data = {"Embed": filt[1].replace('\"','').strip(), "URL": URL}
with open("Video.json", "w") as write_file:
    json.dump(Data, write_file)