from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages




def receipes(request):
    if request.method == "POST":
        receipe_name = request.POST.get('receipe_name')
        receipe_description = request.POST.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')

        if receipe_name and receipe_description and receipe_image:
            Recipe.objects.create(
                receipe_name=receipe_name,
                receipe_description=receipe_description,
                receipe_image=receipe_image,
            )
        return redirect('receipes')

    queryset = Recipe.objects.all()
    context = {'receipes': queryset}
    return render(request, 'receipes.html', context)

def delete_receipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    recipe.delete()
    return redirect('receipes')

def update_receipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)

    if request.method == "POST":
        recipe.receipe_name = request.POST.get('receipe_name')
        recipe.receipe_description = request.POST.get('receipe_description')

        # Only update image if a new one is uploaded
        if request.FILES.get('receipe_image'):
            recipe.receipe_image = request.FILES.get('receipe_image')

        recipe.save()
        return redirect('receipes')

    context = {'recipe': recipe}
    return render(request, 'update_receipe.html', context)


def register_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, "Account created successfully. Please log in.")
            return redirect("login_page")

    return render(request, "register.html")


def login_page(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user_obj = User.objects.get(email=email)
            user = authenticate(request, username=user_obj.username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "Login successful.")
                return redirect("home")  
            else:
                messages.error(request, "Invalid credentials.")
        except User.DoesNotExist:
            messages.error(request, "No account found with that email.")

    return render(request, "login.html")

def logout_page(request):
    logout(request)
    return('/login/')