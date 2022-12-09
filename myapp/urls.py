from django.urls import path,include
from django.conf import settings
from . import views
from . views import *

from .views import  UserDetailAPI,RegisterUserAPIView



from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from myapp.views import  LogoutView
urlpatterns = [
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    path('' , views.index,),
    path('api/register/',RegisterUserAPIView.as_view()),
    path('getpostalldevices/',alldevice.as_view(),name='token_obtain_pair'),
    
]