from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context = {'request': request})
        serializer.is_valid(raise_exception = True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user) 
        return Response({
            'token':token.key,
            'user_id': user.id,
            'email':user.email
        })
    
# This Signal genrate token for new users
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def Genrate_New_Auth_Token(sender, instance=None , created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)