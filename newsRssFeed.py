from bs4 import BeautifulSoup
import requests
import sys

class bcolors:
    WARNING = '\033[93m'
    ENDC = '\033[0m'


if len(sys.argv) > 1:
    link = sys.argv[1]
else:
    print("Add a link to parse it")
    quit()

url = requests.get(link)
soup = BeautifulSoup(url.content, 'xml')
items = soup.find_all('item')

for item in items:
    title = item.title.text
    description = item.description.text
    print(f"{bcolors.WARNING}{title}{bcolors.ENDC}")
    print(description, '\n')
