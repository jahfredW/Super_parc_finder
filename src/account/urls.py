from django.urls import path
from account.views import signup
app_name = "account"


urlpatterns = [
path('', signup, name="signup"),
    ]