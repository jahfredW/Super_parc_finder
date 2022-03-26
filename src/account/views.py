from django.http import HttpResponse
from django.shortcuts import render
from django.db import IntegrityError

from account.models import CustomUSer
# Create your views here.
def signup(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        if password1 != password2:
            return render(request, 'account/signup.html', {"error": "Les mots de passe sont différents"})
        try:
            CustomUSer.objects.create_user(email=email, password=password1)
        except IntegrityError:
            return render(request, 'account/signup.html', {"error": "L'adresse mail existe déja"})

        return HttpResponse(f"Bienvenue : {email.split('@')[0]}")

    return render(request, 'account/signup.html')