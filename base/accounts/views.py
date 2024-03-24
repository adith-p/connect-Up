from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serializers import UserProfileSerializer

# Create your views here.

class GetUserView(APIView):
    def get_user(self,username:str):
        return User.objects.filter(username = username)
    
    def get(self,username:str):
        user_instance = self.get_user(username)
        serializer = UserProfileSerializer(user_instance)
        return Response(data={serializer.data})

        
