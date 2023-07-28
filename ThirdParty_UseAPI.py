'''
This is Third party Python program doesn't have any relation of using django That is a specific programs for test third party use api
Third Party Means Other Programing language's such as c++ , java , react, node etc & also Softwares , android applications
How third party App use this API
'''

import requests
import json
import datetime

print('Application Will Running')
today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")



GET_URL = "http://localhost:8000/"              # Get data 
# ResponseURL = requests.get(url=GET_URL)
# print( f' {ResponseURL.json()} \n\n' )



POST_URl = "http://localhost:8000/NewStudent/"  # Post data 
data = {
    
    'name':'aditya',         # THIS FIELDS HAVE validations 
    'roll':'43',
    'city':'nagpur',
    'created_dt': today
}
JsonData = json.dumps(data)                      # convert data to Json
# responsePOST = requests.post(url=POST_URl, data=JsonData)
# print( f' {responsePOST.json()} \n\n' )



CurdURL = "http://localhost:8000/StudentClassAPI/"
def FetchStudent(id = None):                    # Read < Class Based View >
    data = {}
    if id is not None:
        data = {'id': id}
    JsonData = json.dumps(data)
    responseGET = requests.get(url= CurdURL, data=JsonData)
    return  responseGET.json()
# print(FetchStudent(1))



#  CRUD 
CurdURL = "http://localhost:8000/StudentAPI/"
def FetchStudent(id = None):                    # Read < Function Based View >
    data = {}
    if id is not None:
        data = {'id': id}
    JsonData = json.dumps(data)
    responseGET = requests.get(url= CurdURL, data=JsonData)
    return responseGET.json()
# print(FetchStudent())



def PostStudent():                             # Create
    data = {
        'name':'New user',
        'roll':'67',
        'city':'banglore',
        'created_dt':today,
    }
    JsonData = json.dumps(data)
    ResponsePOST = requests.post(url= CurdURL, data= JsonData)
    return ResponsePOST.json()
# print(PostStudent())



def UpdateStudent():                          # update Seleted fields
    data = {
        'id':1,
        'name':'adarsh',
        'created_dt':today
    }
    JsonData = json.dumps(data)
    ResponseUpdate = requests.put(url= CurdURL, data= JsonData)
    return ResponseUpdate.json()
# print(UpdateStudent())



def UpdateStudentAll():                        # update All fields
    data = {
        'id':1,
        'name':'aditya',
        'roll':'44',
        'city':'nagpur',
        'created_dt':today
    }
    JsonData = json.dumps(data)
    ResponseUpdate = requests.put(url= CurdURL, data= JsonData)
    return ResponseUpdate.json()
# print(UpdateStudentAll())



def DeleteStudent():                            # Delete Student
    data = {
        'id':7,
    }
    JsonData = json.dumps(data)
    ResponseUpdate = requests.delete(url= CurdURL, data= JsonData)
    return ResponseUpdate.json()
# print(DeleteStudent())



API_View_URL = "http://localhost:8000/response/"            # API VIEW
def response():
    data = {
        'name':'vedant'
    }
    headers = {'content-Type':'application/json'}
    responses = requests.post(url= API_View_URL, headers=headers, data= json.dumps(data))
    return responses.json()
# print(response())



CURD_API_URL = "http://localhost:8000/CRUD_func/"           # CRUD API View
def CRUD_func(id = None):
    data = {}
    if id is not None:
        data = {'id': id}
    JsonData = json.dumps(data)
    header = {'content-Type':'application/json'}
    JsonResponse = requests.get(url= CURD_API_URL, headers=header, data=JsonData)
    return JsonResponse.json()
# print(CRUD_func())



def CRUD_func_post():
    data = {
        'name':'ADITYA',
        'roll':'43',
        'city':'delhi'
    }
    JsonData = json.dumps(data)
    headers = {'content-Type':'application/json'}
    JsonResponse = requests.post(url= CURD_API_URL,headers=headers,  data=JsonData)
    return JsonResponse.json()
# print(CRUD_func_post())



def CRUD_func_put():
    data = {
        'id': '1',
        'name':'aditya',
        'roll':'43',
        'city':'Narendra nagar',
        'created_dt':today
    }
    JsonData = json.dumps(data)
    headers = {'content-Type':'application/json'}
    JsonResponse = requests.put(url=CURD_API_URL, headers=headers, data=JsonData)
    return JsonResponse.json()
# print(CRUD_func_put())



def CRUD_func_partial_update():
    data = {
        'id':'1',
        'name':'SAMIR',
        'city':'Chennai'
    }
    JsonData = json.dumps(data)
    headers = {'content-Type':'application/json'}
    JsonResponse = requests.put(url=CURD_API_URL, data=JsonData, headers=headers)
    return JsonResponse.json()
# print(CRUD_func_partial_update())



def CRUD_func_delete():
    data = {
        'id': 16
    }
    JsonData = json.dumps(data)
    headers = {'content-Type':'application/json'}
    JsonResponse = requests.delete(url=CURD_API_URL, data=JsonData, headers=headers)
    return JsonResponse.json()
print(CRUD_func_delete())