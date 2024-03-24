from django.db import models
import uuid
# Create your models here.

class Post(models):
    post_id = models.UUIDField()