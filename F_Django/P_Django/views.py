from django.shortcuts import render, redirect, get_object_or_404
from .models import Quartier, Maison
from .forms import QuartierForm, MaisonForm
from django.contrib import messages

def home(request):
    quartiers = Quartier.objects.all()
    return render(request, 'home.html', {'quartiers': quartiers})

def quartier_detail(request, quartier_id):
    quartier = get_object_or_404(Quartier, id=quartier_id)
    return render(request, 'quartier_detail.html', {'quartier': quartier})

def maison_detail(request, maison_id):
    maison = get_object_or_404(Maison, id=maison_id)
    return render(request, 'maison_detail.html', {'maison': maison})

def creer_quartier(request):
    form = QuartierForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'creer_quartier.html', {'form': form})

def creer_maison(request):
    form = MaisonForm(request.POST or None)
    if form.is_valid():
        try:
            form.save()
            return redirect('home')
        except ValueError as e:
            messages.error(request, str(e))
    return render(request, 'creer_maison.html', {'form': form})

# Create your views here.
