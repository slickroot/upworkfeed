import xml.etree.ElementTree as ET
root = ET.parse('feed.xml').getroot()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

for item in root.findall('channel/item'):
    title = item.find('title').text
    description = item.find('description').text
    print(f"{bcolors.WARNING}{title}{bcolors.ENDC}")
    print(description)
