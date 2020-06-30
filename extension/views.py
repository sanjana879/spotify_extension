from urllib import request

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render
from .api_py import search_results
# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView
from.forms import SearchForm, StartForm
from .models import Results
from django.http import HttpResponse, HttpResponseRedirect


class HomePageView(TemplateView):
    template_name = "index.html"
    success_url = '/awesome/'
    form_class = StartForm()
    def get(self,request):
        return render(request, "index.html", {'form': StartForm()})
    #def form_valid(self, form):


class AboutPageView(TemplateView):
    template_name = "results.html"



class SearchOptions(TemplateView):
    template_name = "results.html"
    success_url = '/awesome/'
    #return render()

def home_page(request):
    return render(request, "index.html", {'form': StartForm()})

def search(request):
    submitted = False
    if request.method == 'GET':
        form = StartForm(request.GET)
    if form.is_valid():
        cd = form.cleaned_data
        names, artists, images = search_results.search_res(cd['option'], cd['name'])
        # add to database
        for name in names:
            post = Results()
            post.name = name
            #post.artist = artist
            #post.img = img
            #post.save()
        # assert False
        mylist = zip(names, artists)

        return render(request, 'results.html', {'option': cd['option'], 'title': cd['name'], 'names': names, 'artists': artists, 'zipped': mylist})
    else:
        form = StartForm()
    if 'submitted' in request.GET:
        submitted = True

    return render(request, 'results.html', {'cd': form, 'submitted': submitted})


def choose(self, request):
    
