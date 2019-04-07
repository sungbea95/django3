'''
Created on 2019. 3. 31.

@author: A
'''
from customlogin.views import *
from django.urls.conf import path
app_name='cl'
urlpatterns = [
    path('signup/', signup, name='signup'),
    #127.0.0.1:8000/cl/signin
    path('signin/', signin, name='signin'),
    #127.0.0.1:8000/cl/signout
    path('signout/', signout, name='signout')
    ]






