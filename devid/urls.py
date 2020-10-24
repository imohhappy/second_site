from django.urls import path
from .views import marriageview
from . import views
app_name = 'devid'
urlpatterns= [
    path('', marriageview, name='case'),
    path('log/', views.log, name='log')
]