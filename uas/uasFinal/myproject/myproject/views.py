from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Project
from .forms import ProjectForm

@login_required
def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.client = request.user
            project.save()
            return redirect('dashboard')
        else:
            # Provide feedback if the form is invalid
            return render(request, 'projects/create_project.html', {'form': form, 'error': 'Form is invalid. Please correct the errors.'})
    else:
        form = ProjectForm()
    return render(request, 'projects/create_project.html', {'form': form})

def home(request):
    return render(request, 'home.html')

def buat_proyek(request):
    return render(request, 'buat_proyek.html')

def cari_freelance(request):
    return render(request, 'cari_freelancer.html') 

def kelola_proyek(request):
    return render(request, 'kelola.html')

def penilaian(request):
    return render(request, 'penilaian.html')
