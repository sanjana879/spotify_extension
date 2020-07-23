
from django.conf.urls import url
from extension import views
from django.views.generic import TemplateView
urlpatterns = [
    #url(r'^results/$', views.SearchOptions.as_view()),
    url(r'^$', views.choose),
    url(r'^results/$', views.search),  # Add this /about/ route
    url(r'^dashboard/$',views.choose),
]

