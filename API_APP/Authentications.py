from rest_framework.permissions import BasePermission

'''
Third Party Permission Packages  --- Pending
1. DRF - Access Policy
2. Compossed Perssions
3. Rest Conditions
4. Dry Rest Permissions
5. Django Rest Framework Roles
6. Django Rest Framework API Key
7. Django Rest Framework Role Filter
7. Django Rest Framework PSQ

Write your Functions like ' verify user '

'''

class Method_Permissions(BasePermission):
    def has_permission(self, request, view):
        '''
        
        '''
        if request.method == " GET":
            return True
        if request.method == "POST":
            return True
        return False
    
    
from rest_framework.authentication import BaseAuthentication
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed

class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        username = request.GET.get('username')
        if not User.objects.filter(username = username).exists():
            return None
        else:
            try:
                User.objects.get(username = username)
            except User.DoesNotExist:
                raise AuthenticationFailed("Username Not Match")
        return User