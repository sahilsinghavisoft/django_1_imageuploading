from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.indexpage,name='index'),
    path('upload/',views.uploadimage,name='imageupload'),
    path('showing/',views.imagefetch,name='show')
]