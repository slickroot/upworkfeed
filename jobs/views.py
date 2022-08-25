from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
from django.template import loader
import requests
import sys
import json


def index(request):
    
    return HttpResponse("Hello Home page")
	
def rss(request):
    template = loader.get_template('rss.html')
    with open('C:/Projects/mysite/config.json') as config_file:
        data = json.load(config_file)

    link = data['link']
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
		
def load(request):
   
    with open('C:/Projects/mysite/config.json') as config_file:
        data = json.load(config_file)

    link = data['link']
    offset = request.POST['offset']
    url = requests.get(link+'&page='+ offset)
    soup = BeautifulSoup(url.content, 'xml')
    items = soup.find_all('item')
   
    array = []
    for item in items:
        title = item.title.text
        description = item.description.text
		
        array.append({'title':title, 'description':description})
		
    context = {
        'items': array
	}
	
    return JsonResponse(data=context)

	