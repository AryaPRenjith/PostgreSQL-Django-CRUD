from django.shortcuts import render
from .models import EmpModel
from django.contrib import messages
#from .forms import EmpForm
from App.forms import EmpForm

# Create your views here.

def showemp(request):
    showall=EmpModel.objects.all()
    return render(request,'index.html',{'data': showall})

def insertemp(request):
    if request.method=='POST':
        if request.POST.get('empname') and request.POST.get('email') and request.POST.get('occupation') and request.POST.get('salary') and request.POST.get('gender'):
            saverecord=EmpModel()
            saverecord.empname=request.POST.get('empname')
            saverecord.email=request.POST.get('email')
            saverecord.occupation=request.POST.get('occupation')
            saverecord.salary=request.POST.get('salary')
            saverecord.gender=request.POST.get('gender')
            saverecord.save()
            messages.success(request, 'Employee' + saverecord.empname + 'is saved successfully..')
            return render(request,'insert.html')
    else:
        return render(request,"insert.html")


def editemp(request,id):
    editempobj=EmpModel.objects.get(id=id)
    return render(request,'edit.html', {'EmpModel': editempobj})

def updateemp(request,id):
    updateemp=EmpModel.objects.get(id=id)
    forms=EmpForm(request.POST, instance=updateemp)
    
    if forms.is_valid():
        forms.save()
        messages.success(request,'Record updated successfully')
        return render(request,'edit.html',{'EmpModel':updateemp })
       
    # else: 
    #     messages.success(request,'Record Not updated')
    #     return render(request,'edit.html',{'EmpModel':updateemp })       

def delemp(request,id):
    delemployee=EmpModel.objects.get(id=id)
    delemployee.delete()
    showdata=EmpModel.objects.all()
    return render(request,'index.html', {'data':showdata})