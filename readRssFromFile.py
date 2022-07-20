import xml.etree.ElementTree as ET
import sys
feed = sys.argv[1]
root = ET.parse(feed).getroot()

class bcolors:
    WARNING = '\033[93m'
    ENDC = '\033[0m'

for item in root.findall('channel/item'):
    title = item.find('title').text
    description = item.find('description').text
    print(f"{bcolors.WARNING}{title}{bcolors.ENDC}")
    print(description)
