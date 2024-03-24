from django.urls import path
from . import views

urlpatterns = [
    path('users/<str:username>/',views.GetUserView.as_view()),
    path('uers/<str:username>/',views.GetUserView.as_view())


]
