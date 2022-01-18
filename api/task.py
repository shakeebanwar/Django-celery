from celery import shared_task
from time import sleep


@shared_task
def sleepy(duration):
    print("calling")
    sleep(duration)
    return {'status':True,'message':'Hourly task executed successfully'}

@shared_task
def emailsend(duration):
    print("sending")
    sleep(duration)
    return {'status':True,'message':'email send successfully'}
