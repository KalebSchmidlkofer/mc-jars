from django.urls import path, include
from django.contrib.auth.models import User

urlpatterns = [
  path('api-auth/', include('rest_framework.urls'))
]
