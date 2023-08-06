from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from urllib import request
from django.shortcuts import render,redirect
import json

# Create your views here.
class HomePageView(View):
    template_name = 'dashboard.html'

    def __init__(self):

        self.moviedata = ''
        with open('moviedata.json', 'r') as json_file:
            self.moviedata = json.load(json_file)
        # print(self.moviedata)
        

    def get(self,request):
        search_input = request.GET.get('searcharea') or ''
        print(search_input)
        context = {'moviedata':self.moviedata}
        return render(request,self.template_name,context)
