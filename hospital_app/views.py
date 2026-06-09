from django.shortcuts import render,redirect
from .models import Department,Doctors
from .forms import  Booking_form

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def booking(request):
    form = Booking_form()
    if request.method == 'POST':
        form = Booking_form(request.POST)
        if form.is_valid():
            form.save()

            return render(request,'confirmation.html')

    return render (request,'booking.html',{'form':form})

def doctors(request):
    doctor = Doctors.objects.all()
    return render (request,'doctors.html',{'doc':doctor})

def contact(request):
    return render (request,'contact.html')

def department(request):
    department = Department.objects.all()
    return render (request,'department.html',{'dept':department})


def confirmation(request):
    return render(request,'confirmation.html')