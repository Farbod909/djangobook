from django.conf.urls import url
from . import views

app_name = "books"

urlpatterns = [
    # GET, POST: /books/
    url(r'^$', views.index, name='index'),
    # GET: /books/create
    url(r'^create/$', views.create, name='create')
]
