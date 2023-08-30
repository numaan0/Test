from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


req = Request("https://ful.io/")
html_page = urlopen(req)


#soup = BeautifulSoup(html_page, "lxml")
testlinks=0
links = []

socialLinks="Social Links \n"
mails="Mail/s \n"
contact= "Contact Number"
for link in soup.findAll('a'):
    links.append(link.get('href'))
    
for i in links:
    if "linked" in i or "facebook" in i:
        socialLinks+=i+"\n"
    if "mailto" in i:
        mails+=i+"\n"
    if "tel" in i:
        contact+=i+""

print(socialLinks)
print(mails)
print(contact.replace('tel',""))
print("aacc")

