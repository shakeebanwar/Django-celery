from django.shortcuts import render
from django.http import JsonResponse
from api.task import *

# Create your views here.

def index(request):
    sleepy.delay(10)
    return JsonResponse({'status':True,'message':'hourly executed'})




def sendemail(request):
    emailsend.delay(15)
    return JsonResponse({'status':True,'message':'email send successfully'})
