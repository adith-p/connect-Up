from rest_framework.serializers import ModelSerializer
from .models import User

class UserProfileSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = User

    