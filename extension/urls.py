
from django.conf.urls import url
from extension import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    #url(r'^about/$', views.AboutPageView.as_view()), # Add this /about/ route
]