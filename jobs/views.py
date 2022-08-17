from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
from django.template import loader
import requests
import sys

def index(request):
    
    return HttpResponse("Hello Home page")
	
	
def form(request):
    template = loader.get_template('form.html')
    return HttpResponse(template.render({}, request))

  
def rss(request):
    template = loader.get_template('rss.html')
    if 'link' in request.POST and request.POST['link']:
        link = request.POST['link']
        url = requests.get(link)
        soup = BeautifulSoup(url.content, 'xml')
        items = soup.find_all('item')
	   
        array = []
        for item in items:
            title = item.title.text
            description = item.description.text
			
		
            array.append({'title':title, 'description':description})
			
        context = {
            'items': array,
            'link': ' the link '+link
        }
        return HttpResponse(template.render(context, request))
	  
    else:
        file = request.FILES.get('xmlFile')
        if file:
            root = ET.parse(file).getroot()
            array = []
            for item in root.findall('channel/item'):
                title = item.find('title').text
                description = item.find('description').text
                array.append({'title':title, 'description':description})

            context = {
                'items': array,
                'file': ' the file '
	        }
        return HttpResponse(template.render(context, request))
    

	
   