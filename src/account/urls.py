from django.urls import path, include
from account.views import signup
app_name = "account"


urlpatterns = [
path('', signup, name="signup"),
    ]

import django.contrib.auth.urls