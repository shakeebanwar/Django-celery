from django.shortcuts import render
from django.http import JsonResponse
from api.task import *
from django.core.mail import EmailMultiAlternatives

# Create your views here.

def index(request):
    sleepy.delay(10)
    return JsonResponse({'status':True,'message':'hourly executed'})




def sendemail(request):
    data = {'email':["shakeebanwar250@gmail.com","shoaibbilal101@gmail.com"]}
    emailsend.delay(data)
    return JsonResponse({'status':True,'message':'email send successfully'})
