from extension.api_py.main import analyze
from django.http import HttpResponse, HttpResponseRedirect
from .models import Results
from urllib import request

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render
from .api_py import search_results, analysis
# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView
from.forms import SearchForm, StartForm, ResultForm


class HomePageView(TemplateView):
    template_name = "index.html"
    success_url = '/awesome/'
    form_class = StartForm()

    def get(self, request):
        return render(request, "index.html", {'form': StartForm()})
    # def form_valid(self, form):


class AboutPageView(TemplateView):
    template_name = "results.html"


class SearchOptions(TemplateView):
    template_name = "results.html"
    success_url = '/awesome/'
    # return render()


def home_page(request):
    return render(request, "index.html", {'form': StartForm()})


global type_option


def search(request):
    submitted = False
    if request.method == 'GET':
        form = StartForm(request.GET)
    if form.is_valid():
        cd = form.cleaned_data
        global type_option
        type_option = cd['option']
        names, artists, images, uris = search_results.search_res(
            cd['option'], cd['name'])
        # add to database
        for name in names:
            post = Results()
            post.name = name
            #post.artist = artist
            #post.img = img
            # post.save()
        # assert False
        mylist = zip(names, artists, uris)

        return render(request, 'results.html', {'option': cd['option'], 'title': cd['name'], 'names': names, 'artists': artists, 'zipped': mylist, 'uris': uris})
    else:
        form = StartForm()
    if 'submitted' in request.GET:
        submitted = True

    return render(request, 'results.html', {'cd': form, 'submitted': submitted})


def choose(request):

    if request.method == 'GET':
        form = ResultForm(request.GET)

    # if form.is_valid():
        #val = form.cleaned_data.get("btn")
        # print(type_option)
        val = 'spotify:album:2QJmrSgbdM35R67eoGQo4j'
        type_option = 'album'
        music_features, title, sentiment, moods = analyze(val, type_option)
        return render(request, 'dashboard.html', {'music_features': music_features, 'title': title, 'sentiment': sentiment, 'moods': moods})
    # else:
        #form = ResultForm()
    # return render(request, 'dashboard.html', locals())
