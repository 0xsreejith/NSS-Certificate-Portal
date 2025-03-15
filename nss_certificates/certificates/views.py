from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import Certificate, Student
from .forms import CertificateUploadForm, CustomUserCreationForm

def home(request):
    return render(request, 'certificates/home.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Student.objects.create(user=user, roll_number=f"ROLL{user.id}", department="NSS")
            login(request, user)
            return redirect('student_certificates')
    else:
        form = CustomUserCreationForm()
    return render(request, 'certificates/register.html', {'form': form})

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('student_certificates')
    else:
        form = AuthenticationForm()
    return render(request, 'certificates/login.html', {'form': form})

def custom_logout(request):
    logout(request)
    return redirect('login')

@login_required
def upload_certificate(request):
    if request.user.is_superuser:
        if request.method == "POST":
            form = CertificateUploadForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('certificate_list')
        else:
            form = CertificateUploadForm()
        return render(request, 'certificates/upload_certificate.html', {'form': form})
    return redirect('home')

@login_required
def student_certificates(request):
    certificates = Certificate.objects.filter(student__user=request.user, approved=True)
    return render(request, 'certificates/student_certificates.html', {'certificates': certificates})

@login_required
def certificate_list(request):
    if request.user.is_superuser:
        certificates = Certificate.objects.all()
        return render(request, 'certificates/approve_certificates.html', {'certificates': certificates})
    return redirect('home')

@login_required
def approve_certificate(request, cert_id):
    if request.user.is_superuser:
        certificate = get_object_or_404(Certificate, id=cert_id)
        certificate.approved = True
        certificate.save()
    return redirect('certificate_list')
