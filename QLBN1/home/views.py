from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

from django.shortcuts import redirect, render,redirect
from .forms import PatientForm
from collections import deque
import datetime
from .models import Patient
from django.contrib import messages
# Create your views here.

""" def queue(request):
    patients = Patient.objects.filter().order_by('NameP')
    return render(request, 'list.html', {}) """


def patient_create(request):
    if request.method == "POST":
        idP = request.POST.get('nameID')
        NameP = request.POST.get('nameP')
        Dob_str = request.POST.get('DOB', '')  
        if Dob_str:  
            try:
                Dob = datetime.datetime.strptime(Dob_str, '%Y-%m-%d')
            except ValueError:
                Dob = None
        else:
            Dob = None
        
        Gender = request.POST.get('Sex') == 'Male'
        Phone_Number = request.POST.get('phone_number')
        Address = request.POST.get('address')

        item_patient = Patient(idP=idP, NameP=NameP, Dob=Dob, Gender=Gender, Phone_Number=Phone_Number, Address=Address)
        item_patient.save()

        messages.success(request, 'Đăng ký thành công cho bệnh nhân')
        return redirect('/')  # Assuming 'queue' is the name of the URL to which you want to redirect after successful creation

    return render(request, 'create.html', {})


def patient_list(request):
    # Retrieve all patient objects from the database
    patients = Patient.objects.all()
    # Pass the patient data to the template for rendering
    return render(request, 'list.html', {'patients': patients})


def patient_update(request,idP):
     item_patient=Patient.objects.get(id=idP)
     if request.method == "POST":
        idP = request.POST.get('nameID')
        NameP = request.POST.get('nameP')
        Dob_str = request.POST.get('DOB', '')  
        if Dob_str:  
            try:
                Dob = datetime.datetime.strptime(Dob_str, '%Y-%m-%d')
            except ValueError:
                Dob = None
        else:
            Dob = None
        
        Gender = request.POST.get('Sex') == 'Male'
        Phone_Number = request.POST.get('phone_number')
        Address = request.POST.get('address')

        item_patient = Patient(idP=idP, NameP=NameP, Dob=Dob, Gender=Gender, Phone_Number=Phone_Number, Address=Address)
        item_patient.save()

        messages.success(request, 'Đăng ký thành công cho bệnh nhân')
        return redirect('/')
    
     return render(request,'update.html',{'item_patient':item_patient})