from . import views
from django.urls import path
from.views import (
    Vacancydetail, Contact, Postdetail, about,
    Vacancyview, Studentcreatview, VancancyDelete, VancancyUpdate
)


app_name = 'job'

urlpatterns = [
    path('contact/', Contact.as_view(), name='contact'),
    path('', Vacancyview.as_view(), name='vacancy'),
    path('<int:pk>/', Vacancydetail.as_view(), name='detail'),
    path('update/<int:pk>/', VancancyUpdate.as_view(), name='Vupdate'),
    path('<int:pk>/delete/', VancancyDelete.as_view(), name='Vdelete'),
    path('<int:vacancy_id>/<int:pk>', Postdetail.as_view(), name='postkeep'),
    path('about/', about, name='about'),
    path('comment/', views.contactview, name='comment'),
    path('up/', views.up, name='update'),
    path('create/vacancy', Studentcreatview.as_view(), name='create')
]