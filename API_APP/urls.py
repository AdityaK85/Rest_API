from django.urls import path, include

from .CustomToken import CustomAuthToken
from .views import *
from .cron import *
from .Authentications import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('Student_Class_View_Set', Student_Class_View_Set, basename="view_set_api")          #Work Only in ViewSet Classes
router.register('Student_Model_View_Set', Student_Model_View_Set, basename="Model view_set_api")    #Work Only in ViewSet Classes
router.register('Student_Read_Only_Model_View_Set', Student_Read_Only_Model_View_Set, basename="Read Only Model view_set_api")    #Work Only in ViewSet Classes


urlpatterns = [
    path('', GetStudent),
    path('NewStudent/', NewStudent),

     path('login/', Login.as_view()),                                           # DRF Class Based View  < API VIEW >
     path('verify_otp/', Verify_otp.as_view()),                                 # DRF Class Based View  < API VIEW >
     path('registers/', Registers.as_view()),                                   # DRF Class Based View  < API VIEW >
    
    path('StudentAPI/', StudentAPI),                                            # Function Based View
    path('StudentClassAPI/', StudentClassAPI.as_view()),                        # Class Based View

    path('response/', response),                                                # Django Function Based View  < API VIEW >
    path('CRUD_func/', CRUD_func),                                              # Django Function Based View  < API VIEW >
    path('CRUD_func/<int:id>', CRUD_func),                                      # Django Function Based View  < API VIEW >

    path('Student_DRF_Class_API_View/', Student_DRF_Class_API_View.as_view()),  # DRF Class Based View  < API VIEW >
    path('Student_DRF_Class_API_View/<int:id>', Student_DRF_Class_API_View.as_view()),  # DRF Class Based View  < API VIEW >

    path('Class_Genrice_api_view/', Class_Genrice_api_view.as_view()),           # DRF Class Based View  < Genrice API VIEW & Group MIXINS  GET & CREATE >
    path('Class_Genrice_api_view/<int:pk>', Class_Genrice_api_view_put_delete.as_view()),  # DRF Class Based View  < Genrice API VIEW & Group MIXINS  UPDATE & DELETE >

    path('Genrice_CR/', Genrice_CR.as_view()),                                  # DRF Class Based View  < Genrice API VIEW  >
    path('Genrice_CR/<int:pk>', Genrice_UD.as_view()),                          # DRF Class Based View  < Genrice API VIEW >

    path('Student_GET_POST/', Student_GET_POST.as_view()),                      # DRF Class Based View  < Genrice API VIEW  METHODS >
    path('Student_GET_POST/<int:pk>', Student_UPDATE_GET_DELETE.as_view()),     # DRF Class Based View  < Genrice API VIEW METHODS >

    path('api/', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace="Rest Framework Login")),

    path('GET_Token/', CustomAuthToken.as_view()),
]