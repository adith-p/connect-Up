from django.db import models

from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.

class User(AbstractUser):
    user_id = models.UUIDField(primary_key=True,default=uuid.uuid4,name='user_id')
    bio = models.TextField(max_length=180)
    image_url = models.ImageField()




    
