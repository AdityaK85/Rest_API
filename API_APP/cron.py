from django.http import JsonResponse
from .serializer import *
from .models import *
from .views import *
import json
from django.views.decorators.csrf import csrf_exempt
import traceback
import requests
import json
import datetime

today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

CurdURL = "http://localhost:8000/StudentAPI/"

def PostStudent():                             # Create
    print('Crontab Will Running*****************************************************')
    print('********************************------Cron------------*******************')
    data = {
        'name':'cron user',
        'roll':'67',
        'city':'banglore',
        'created_dt':today,
    }
    JsonData = json.dumps(data)
    ResponsePOST = requests.post(url= CurdURL, data= JsonData)
    return ResponsePOST.json()


import logging
logger = logging.getLogger(__name__)

def print_hello():
    print('Cron Tab----------- run')
    logger.info("Cron Job Called ")