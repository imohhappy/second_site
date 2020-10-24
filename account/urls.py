from django.urls import path
from . views import Signupview, Loginview, Logoutview, Passwordview, Passwordresetview, Setpasswordview, Passwordchangeview
app_name = 'account'


urlpatterns = [
    path('date/', Signupview.as_view(), name='signup'),
    path('', Loginview.as_view(), name='login'),
    path('logout/', Logoutview.as_view(), name='logout'),
    path('pass/', Passwordview.as_view(), name='pass'),
    path('rest/', Passwordresetview.as_view(), name='rest'),
    path('new/', Setpasswordview.as_view(), name='new'),
    path('word/', Passwordchangeview.as_view(), name='word')
]