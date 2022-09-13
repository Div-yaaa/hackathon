from django.urls import path
from .views import *

urlpatterns = [
    path('sales/register', SalesRegistrationView.as_view(), name="register POST"),
    path('login', LoginView.as_view(), name="login POST"),
    path('get/developer', DeveloperApi.as_view(), name="developer GET"),
    path('post/developer', DeveloperApi.as_view(), name="developer POST"),
    path('patch/developer', DeveloperApi.as_view(), name="developer PATCH"),
    path('get/project', ProjectApi.as_view(), name="project GET"),
    path('post/project', ProjectApi.as_view(), name="project POST"),
    path('get/cilent', CilentApi.as_view(), name="cilent GET"),
    path('post/cilent', CilentApi.as_view(), name="cilent POST"),
    path('schedule/meeting', Scheduled_call.as_view(), name="scheduled POST"),
]
