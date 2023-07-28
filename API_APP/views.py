from django.http import JsonResponse
from .serializer import *
from .models import *
import json
from django.views.decorators.csrf import csrf_exempt
import traceback
import random

def GetStudent(request):
    stu = Student.objects.all()
    serializers = StudentSerializers(stu, many= True)
    return JsonResponse(serializers.data,safe=False)

def NewStudent(request):
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        serializers = StudentSerializers(data=data)
        if serializers.is_valid() :
            serializers.save()
            send_data = {'msg':'created', 'send data':data}
            return JsonResponse(send_data, safe=False)
        else:
            send_data = {'msg':'created', 'send data':serializers.errors}
            return JsonResponse(send_data, safe=False)

#  Function Based Views
@csrf_exempt
def StudentAPI(request):
    data = json.loads(request.body.decode('utf-8'))
    if request.method == "GET":
        id = data.get('id', None)
        if id is not None:
            stu = Student.objects.get(id = id)
            serializers = StudentSerializers(stu)
            SendData = {"msg":'Success', 'data':serializers.data}
            return JsonResponse(SendData , safe=False)
        
        else:
            stu = Student.objects.all()
            serializers = StudentSerializers(stu, many = True)
            SendData = {"msg":'Fetch all data', 'data':serializers.data}
            return JsonResponse(SendData , safe=False)
        

    if request.method == "POST":
        serializers = StudentSerializers(data= data) 
        if serializers.is_valid():
            serializers.save()
            SendData = {"msg":'Student Added', 'data':serializers.data}
            return JsonResponse(SendData , safe=False)
        
        send_data = {'msg':'created', 'send data':serializers.errors}
        return JsonResponse(send_data, safe=False)

    if request.method == 'PUT':
        id = data.get('id', None)
        get_stu = Student.objects.get(id = id)
        serializers = StudentSerializers(get_stu, data=data, partial = True)
        if serializers.is_valid():
            serializers.save()
            SendData = {"msg":'Student Updated', 'data':serializers.data}
            return JsonResponse(SendData , safe=False)
        else:
            SendData = {"msg":'Student Not Updated', 'data':serializers.error_messages}
            return JsonResponse(SendData , safe=False)
            

    if request.method == 'PUT':
        id = data.get('id', None)
        get_stu = Student.objects.get(id = id)
        serializers = StudentSerializers(get_stu, data=data )
        if serializers.is_valid():
            serializers.save()
            SendData = {"msg":'Student Updated', 'data':serializers.data}
            return JsonResponse(SendData , safe=False)
        else:
            SendData = {"msg":'Student Not Updated', 'data':serializers.error_messages}
            return JsonResponse(SendData , safe=False)
            

    if request.method == 'DELETE':
        id = data.get('id', None)
        get_stu = Student.objects.get(id = id).delete()
        SendData = {"msg":'Student Deleted'}
        return JsonResponse(SendData , safe=False)
    

# Class Based Views
from django.utils.decorators import method_decorator
from django.views import View

@method_decorator(csrf_exempt, name='dispatch')
class StudentClassAPI(View):

    def get(self,  request, *args, **kwargs):

        data = json.loads(request.body.decode('utf-8'))
        id = data.get('id', None)
        if id is not None:
            stu = Student.objects.get(id = id)
            serializers = StudentSerializers(stu)
            SendData = {"msg":'Success By Using Class Based views', 'data':serializers.data}
            return JsonResponse(SendData , safe=False)
        
        else:
            stu = Student.objects.all()
            serializers = StudentSerializers(stu, many = True)
            SendData = {"msg":'Fetch all data By Using Class Based views', 'data':serializers.data}
            return JsonResponse(SendData , safe=False)
        
    def post(self, request, *args, **kwargs ):
        data = json.loads(request.body.decode('utf-8'))
        serializers = StudentSerializers(data= data) 
        if serializers.is_valid():
            serializers.save()
            SendData = {"msg":'Student Added', 'data':serializers.data}
            return JsonResponse(SendData , safe=False)
        
    def put(self, request, *args, **kwargs):
        data = json.loads(request.body.decode('utf-8'))
        id = data.get('id', None)
        get_stu = Student.objects.get(id = id)
        serializers = StudentSerializers(get_stu, data=data, partial = True)
        if serializers.is_valid():
            serializers.save()
            SendData = {"msg":'Student Updated', 'data':serializers.data}
            return JsonResponse(SendData , safe=False)
        else:
            SendData = {"msg":'Student Not Updated', 'data':serializers.error_messages}
            return JsonResponse(SendData , safe=False)

    def put(self, request, *args, **kwargs):
        data = json.loads(request.body.decode('utf-8'))
        id = data.get('id', None)
        get_stu = Student.objects.get(id = id)
        serializers = StudentSerializers(get_stu, data=data )
        if serializers.is_valid():
            serializers.save()
            SendData = {"msg":'Student Updated', 'data':serializers.data}
            return JsonResponse(SendData , safe=False)
        else:
            SendData = {"msg":'Student Not Updated', 'data':serializers.error_messages}
            return JsonResponse(SendData , safe=False)
        
    def delete(self, request, *args, **kwargs):
        data = json.loads(request.body.decode('utf-8'))
        id = data.get('id', None)
        get_stu = Student.objects.get(id = id).delete()
        SendData = {"msg":'Student Deleted'}
        return JsonResponse(SendData , safe=False)
    
    
from rest_framework.authentication import BasicAuthentication, SessionAuthentication  ,TokenAuthentication         # Authentications
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import authentication_classes, permission_classes

@api_view(['GET','POST'])                                       # API Views
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def response(request):
    if request.method == "POST":
        return Response({'msg':'Post method allowed', 'data':request.data})
    if request.method == "GET":
        return Response({'msg':'GET method allowed', 'data':request.data})


@api_view(['GET','POST', 'PUT', 'PATCH', 'DELETE'])
def CRUD_func(request , id=None):
    try:
        if request.method == 'GET':
            if id is not None:
                serializers = StudentSerializers(Student.objects.get(id = id))
                send_data = {'msg':'Get Method', 'data':serializers.data}
                return Response(send_data)
            else:
                serializers = StudentSerializers(Student.objects.all(), many=True)
                send_data = {'msg':'Get Method', 'data':serializers.data}
                return Response(send_data)

        if request.method == "POST":
            serializers = StudentSerializers(data=request.data)
            if serializers.is_valid():
                serializers.save()
                send_data = {'msg':'POST Method', 'data':serializers.data}
                return Response(send_data)
            send_data = {'msg':'POST Method', 'data':serializers.errors}
            return Response(send_data)

        if request.method == "PUT":
            serializers = StudentSerializers(Student.objects.get(id = request.data.get('id')), data=request.data)
            if serializers.is_valid():
                serializers.save()
                send_data = {'msg':'PUT Method', 'data':serializers.data}
                return Response(send_data)
            send_data = {'msg':'PUT Method', 'data':serializers.errors}
            return Response(send_data)
        
        if request.method == "PUT":
            serializers = StudentSerializers(Student.objects.get(id = request.data.get('id')), request.data)
            if serializers.is_valid():
                serializers.save()
                send_data = {'msg':'PUT Method', 'data':serializers.data}
                return Response(send_data)
            send_data = {'msg':'PUT Method', 'data':serializers.errors}
            return Response(send_data)
        
        if request.method == "PATCH":
            serializers = StudentSerializers(Student.objects.get(id = request.data.get('id')), request.data, partial = True)
            if serializers.is_valid():
                serializers.save()
                send_data = {'msg':'PUT Method', 'data':serializers.data}
                return Response(send_data)
            send_data = {'msg':'PUT Method', 'data':serializers.errors}
            return Response(send_data)
        
        if request.method == "DELETE":
            stu = Student.objects.get(id = id).delete()
            send_data = {'msg':'DELETE Method'}
            return Response(send_data)
        
    except Exception as e:
        print(traceback.print_exc(e))
        send_data = {'msg':'DELETE Method', 'status':'METHOD NOT ALLOWED'}
        return Response(send_data) 

        
from rest_framework.views import APIView

class Registers(APIView):
    def post(self, request):
        data = request.data
        mobile = data['mobile']
        if login.objects.filter(mobile = mobile).exists():
            send_data = {'msg':'mobile already exists'}
            return JsonResponse(send_data, safe=False)
        else:
            serializers = LoginSerializers(data = request.data)
            if serializers.is_valid():
                serializers.save()
                send_data = {'msg':'Signup created'}
                return JsonResponse(send_data, safe=False)
    

class Login(APIView):
    def post(self, request):
        data = request.data
        print(data)
        login
        if login.objects.filter(mobile = data['mobile']).exists():
            obj = login.objects.get(mobile = data['mobile'])
            otp = random.randrange(1000, 10000)
            # otp = '1234'
            print('**********OTP', otp)
            obj.verify_otp = otp
            obj.save()
            send_data = {'msg':'otp sent to your register mobile number'}
        else:
            send_data = {'msg':'invalid mobile number'}
        return JsonResponse(send_data, safe=False)


class Verify_otp(APIView):
    def post(self, request):
        try:
            data = request.data
            mobile = data['mobile']
            otp = data['otp']
            if login.objects.filter(mobile = mobile).exists():
                obj = login.objects.get(mobile = mobile)
                if data['otp'] == obj.verify_otp:
                    obj.verify_otp = otp
                    obj.save()
                    send_data = {'msg':'otp verified successfully'}
                else:
                    send_data = {'msg':'Invalid otp'}
            else:
                send_data = {'msg':'Invalid Mobile number'}
                
        except Exception as e:
            send_data = {'msg':'something went wrong'}
            print(e)
        return JsonResponse(send_data, safe=False)


class Student_DRF_Class_API_View(APIView):                 # Rest Framework Class based API View 
    def get(self, request, id=None):
        if id is not None:
            serializers = StudentSerializers(Student.objects.get(id = id))
            send_data = {'msg':'GET Method', 'data':serializers.data}
            return Response(send_data)
        else:
            serializers = StudentSerializers(Student.objects.all(), many=True)
            send_data = {'msg':'GET Method', 'data':serializers.data}
            return Response(send_data)
        
    def post(self, request):
        serializers = StudentSerializers(data= request.data)
        if serializers.is_valid():
            serializers.save()
            send_data = {'msg':'POST Method', 'data':serializers.data}
            return Response(send_data)
        send_data = {'msg':'created', 'send data':serializers.errors}
        return JsonResponse(send_data, safe=False)

    def put(self, request, id ):
        serializers = StudentSerializers(Student.objects.get(id = id), request.data)
        if serializers.is_valid():
            serializers.save()
            send_data = {'msg':'PUT Method', 'data':serializers.data}
            return Response(send_data)
        send_data = {'msg':'created', 'send data':serializers.errors}
        return JsonResponse(send_data, safe=False)
        
    def patch(self, request, id):
        serializers = StudentSerializers(Student.objects.get(id=id), request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            send_data = {'msg':'PATCH Method', 'data':serializers.data}
            return Response(send_data)
        send_data = {'msg':'created', 'send data':serializers.errors}
        return JsonResponse(send_data, safe=False)
        
    def delete(self, request, id):
        Student.objects.get(id = id).delete()
        send_data = {'msg':'DELETE Method'}
        return Response(send_data)
    

from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin
from rest_framework.generics import GenericAPIView

class Class_Genrice_api_view(GenericAPIView, ListModelMixin, CreateModelMixin ):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class Class_Genrice_api_view_put_delete(GenericAPIView, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin ):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    
    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView , RetrieveAPIView, UpdateAPIView         # Genrics
class Genrice_CR(ListAPIView, CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

class Genrice_UD(DestroyAPIView , RetrieveAPIView, UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
class Student_GET_POST(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

class Student_UPDATE_GET_DELETE(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers



# VIEW SETS
from rest_framework import viewsets
class Student_Class_View_Set(viewsets.ViewSet):

    def list(self,  request):
        stu = Student.objects.all()
        serializers = StudentSerializers(stu, many = True)
        SendData = {"msg":'Fetch all data By Using Class Based views', 'data':serializers.data}
        return Response(SendData)
        
    def retrieve(self,  request, pk=None):
        stu = Student.objects.get(id = pk)
        serializers = StudentSerializers(stu)
        SendData = {"msg":'Retrieve Class Based views', 'data':serializers.data}
        return Response(SendData)
      
    def create(self, request ):
        serializers = StudentSerializers(data= request.data) 
        if serializers.is_valid():
            serializers.save()
            SendData = {"msg":'Student Added', 'data':serializers.data}
            return Response(SendData)
        
    def retrive(self, request, pk):
        get_stu = Student.objects.get(id = pk)
        serializers = StudentSerializers(get_stu, data=request.data)
        if serializers.is_valid():
            serializers.save()
            SendData = {"msg":'Student Updated', 'data':serializers.data}
            return Response(SendData)
        else:
            SendData = {"msg":'Student Not Updated', 'data':serializers.error_messages}
            return Response(SendData)

    def update(self, request, pk):
        get_stu = Student.objects.get(id = pk)
        serializers = StudentSerializers(get_stu, data=request.data )
        if serializers.is_valid():
            serializers.save()
            SendData = {"msg":'Student Updated', 'data':serializers.data}
            return Response(SendData)
        else:
            SendData = {"msg":'Student Not Updated', 'data':serializers.error_messages}
            return Response(SendData)
        
    def destroy(self, request, pk):
        get_stu = Student.objects.get(id = pk).delete()
        SendData = {"msg":'Student Deleted'}
        return Response(SendData)
    
    
from .Authentications import  CustomAuthentication  
class Student_Model_View_Set(viewsets.ModelViewSet):
    authentication_classes = [CustomAuthentication]
    # authentication_classes = [SessionAuthentication]                            # Model View Set CRUD
    # permission_classes = [IsAuthenticatedOrReadOnly]
    permission_classes = [DjangoModelPermissions]
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

from .Authentications import Method_Permissions , CustomAuthentication          # Custom Permission & Authentications

class Student_Read_Only_Model_View_Set(viewsets.ReadOnlyModelViewSet):          # Read Only Model View Set CRUD
    # authentication_classes = [AllowAny]
    # authentication_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]
    
    # permission_classes = [Method_Permissions]
    
    queryset = Student.objects.all()
    serializer_class = StudentSerializers