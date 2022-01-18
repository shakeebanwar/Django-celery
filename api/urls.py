from django.urls import path,include
from api.views import *

urlpatterns = [

#web urls  home
path('',index,name="index"),
path('sendemail',sendemail,name="sendemail"),





]






