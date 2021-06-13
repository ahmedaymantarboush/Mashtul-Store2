from django.urls import path
from .views import *


app_name="UserProfile"

urlpatterns = [
    path("profile" , profile ,name="profile" ),
    path("editProfile" , editProfile ,name="editProfile" ),
    path("editValue" , editValue ,name="editValue" ),
    path("signUp" , signUp ,name="signUp" ),
    path("addAccount" , addAccount ,name="addAccount" ),
    path("signin" , signin ,name="signin" ),
    path("logout" , logout ,name ="logout"),
]