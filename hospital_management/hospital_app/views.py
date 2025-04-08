from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import DoctorRegisterForm, PatientForm # type: ignore
from .models import Patient
from django.contrib.auth.decorators import login_required

def register_doctor(request):
    if request.method == 'POST':
        form = DoctorRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = DoctorRegisterForm()
    return render(request, 'doctor_register.html', {'form': form})

@login_required
def dashboard(request):
    patients = Patient.objects.filter(doctor=request.user)
    query = request.GET.get('q')
    if query:
        patients = patients.filter(name__icontains=query)
    return render(request, 'dashboard.html', {'patients': patients})

@login_required
def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.doctor = request.user
            patient.save()
            return redirect('dashboard')
    else:
        form = PatientForm()
    return render(request, 'add_patient.html', {'form': form})

