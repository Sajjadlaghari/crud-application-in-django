from django.shortcuts import redirect, render
from django.http import HttpResponse
from myapp.models import Employee
from django.contrib import messages


def home(request):
    employees = Employee.objects.all()
    return render(request,'index.html',{'employees':employees})

def addEmployee(request):
    return render(request,'AddEmployee.html')

def createemployee(request):
        if request.method == 'POST':
            if request.POST.get('name') and request.POST.get('email'):
                emp=Employee()
                emp.name= request.POST.get('name')
                emp.email= request.POST.get('email')
                emp.phone= request.POST.get('phone')
                emp.address= request.POST.get('address')
                emp.save()
                messages.success(request, "Employee Added Successfully.")
                return redirect('home')

        else:
                return render(request,'AddEmployee.html')

def edit(request,id):
    record = Employee.objects.get(id=id)
    return render(request,'edit.html',{'record':record})

def update(request):    
    emp = Employee.objects.get(id=request.POST.get('id'))
    emp.name= request.POST.get('name')
    emp.email= request.POST.get('email')
    emp.phone= request.POST.get('phone')
    emp.address= request.POST.get('address')
    emp.save()
    messages.success(request, "Employee Update Successfully.")
    return redirect('home')

def delete(request,id):
    member = Employee.objects.get(id=id)
    member.delete()
    messages.success(request, "Employee Deleted Successfully.")
    return redirect('home')
