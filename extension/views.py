from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView
from.forms import SearchForm
from django.http import HttpResponse

class HomePageView(TemplateView):
    template_name = "index.html"
    success_url = '/awesome/'
    form_class = SearchForm
    if 'search-for' in request.POST:
        if 'search' == request.POST.get('search-for'):
            pass

    def form_valid(self, form):
        return HttpResponse("Sweeeeeet.")






