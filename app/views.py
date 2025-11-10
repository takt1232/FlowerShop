from django.shortcuts import get_object_or_404, redirect, render
from app.models import Flower
from .forms import FlowerForm

# Create your views here.
def landing_page(request):
    return render(request, 'app/landing-page.html')

def flower_list(request):
    flowers = Flower.objects.all()
    return render(request, 'app/flower-list.html', {"flowers": flowers})

def flower_details(request, pk):
    flower = get_object_or_404(Flower, pk=pk)
    return render(request, 'app/flower-details.html', {'flower': flower})

def add_flower(request):
    if request.method == 'POST':
        form = FlowerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('flower_list')
    else:
        form = FlowerForm()
    return render(request, 'app/add-flower.html', {'form': form})

def delete_flower(request, pk):
    flower = get_object_or_404(Flower, pk=pk)
    if request.method == "POST":
        flower.delete()
        return redirect('flower_list')
    return render(request, 'confirm_delete.html', {'flower': flower})
