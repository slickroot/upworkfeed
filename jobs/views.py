from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from bs4 import BeautifulSoup
from django.template import loader
import requests
import sys

def index(request):
    
    return HttpResponse("Hello Home page")
	
	
def form(request):
    template = loader.get_template('form.html')
    test = 'hello world'
    context = {
        'test': test,
		'test2': "hello Africa"
    }
    return HttpResponse(template.render(context, request))

  
def rss(request): 
    link = request.POST['link']
    url = requests.get(link)
    soup = BeautifulSoup(url.content, 'xml')
    items = soup.find_all('item')
    template = loader.get_template('rss.html')
   
    array = []
    for item in items:
        title = item.title.text
        description = item.description.text
        
		
        array.append({'title':title, 'description':description})
		
    context = {
	    'items': array,
		'link': link
    }
	
    return HttpResponse(template.render(context, request))

