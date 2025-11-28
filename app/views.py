from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from app.models import Flower, FlowerCategory
from .forms import FlowerCategoryForm, FlowerForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login

# Create your views here.
def landing_page(request):
    return render(request, 'app/landing-page.html')

def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user:
            auth_login(request, user)
            return redirect('landing_page')
        else:
            messages.error(request, "Invalid login credentials.")

    return render(request, 'app/login.html')

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=email).exists():
            messages.error(request, "Email is already registered.")
            return redirect('register')

        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=name
        )
        user.save()

        messages.success(request, "Account created successfully.")
        return redirect('login')

    return render(request, 'app/register.html')

def flower_category(request):
    categories = FlowerCategory.objects.all()
    return render(request, 'app/flower-category.html', {"categories": categories})

def flower_category_create(request):
    if request.method == 'POST':
        form = FlowerCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('flower_categories')
    else:
        form = FlowerCategoryForm()
    return render(request, 'app/add-flower-category.html', {'form': form})

def flower_list(request, pk):
    category = FlowerCategory.objects.get(pk=pk)
    flowers = Flower.objects.filter(category=category)

    return render(request, "app/flower-list.html", {
        "category": category,
        "flowers": flowers
    })


def flower_details(request, pk):
    flower = get_object_or_404(Flower, pk=pk)
    categories = FlowerCategory.objects.all()
    return render(request, 'app/flower-details.html', {'flower': flower, 'categories': categories})

def add_flower(request):
    if request.method == 'POST':
        form = FlowerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('flower_categories')
    else:
        form = FlowerForm()
    return render(request, 'app/add-flower.html', {'form': form})

def update_flower(request, pk):
    flower = get_object_or_404(Flower, pk=pk)

    if request.method == "POST":
        flower.name = request.POST.get("name")
        flower.category_id = request.POST.get("category")

        if "image" in request.FILES:
            flower.image = request.FILES["image"]

        flower.save()
        return redirect('flower_categories')

    return redirect('flower_detail', pk=pk)

def delete_flower(request, pk):
    flower = get_object_or_404(Flower, pk=pk)
    if request.method == "POST":
        flower.delete()
        return redirect('flower_categories')
    return render(request, 'confirm_delete.html', {'flower': flower})
