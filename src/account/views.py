from django.http import HttpResponse
from django.shortcuts import render, redirect
from account.forms import CustomSignupForm


def signup(request):
    context = {}

    if request.method == "POST":
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("parc:home")
        else:
            context['errors'] = form.errors

    form = CustomSignupForm()
    context["form"] = form

    return render(request, "account/signup.html", context=context)



"""
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
"""