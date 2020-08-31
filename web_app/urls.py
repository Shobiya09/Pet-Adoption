from django.conf.urls import url
from web_app import views

app_name ='web_app'

urlpatterns = [
        url('index/',views.index,name='index'),
        url('about/',views.about,name='about'),
        url('services/',views.services,name='services'),
        url('blog/',views.blog,name='blog'),
        url('contacts/',views.contacts,name='contacts'),
        url('dog/',views.dogcategory,name='dog_category'),
        url('cat/',views.cat,name='cat'),
        url('bird/',views.bird,name='bird'),
        url('upload-pet/',views.upload_pet,name='upload_pet'),
        url('upload/',views.upload,name='upload'),
        url(r'^edit/(?P<pk>\d+)/$', views.edit, name='edit'),
        url('search/',views.search,name='search'),
]
