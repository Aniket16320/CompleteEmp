from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Employee, Role, Department
from django.contrib.auth import authenticate, login,logout
from datetime import datetime
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.


def Signup(request):
     if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        try:
            if password == confirm_password:
                if User.objects.filter(username=username).exists():
                    messages.info(request, 'user is alerady exists')
                    return redirect('Signup')
                else:
                    user = User.objects.create_user(
                        username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    user.set_password(password)
                    user.save()
                    return redirect('login')
        except Exception as e:

           messages = "somting else"
           data = {
            "messages": messages,
           }

           return redirect('Signup')
     else:
        messages="somting else"
        
        data={
        "messages":messages,
        }
        print("error")

     return render(request, 'Signup.html')




def login_user(request):
     if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Invalid user')
            return redirect('/login_user/')
     else : 
        return render(request, 'login.html') 
     return render(request, 'login.html')




@login_required(login_url='locations:login_view')
def index(request):
    return render(request, 'index.html')


def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps':emps
    }

    # for a in emps:
    #    print(a.salary)
 
    # print(emps)
    return render(request, 'view_all_emp.html' , context)

def add_emp(request):
    rol  = Role.objects.all()
    var = Department.objects.all()
    if request.method == 'POST':
      first_name = request.POST.get('first_name')
      last_name = request.POST.get('last_name')
      salary = int(request.POST.get('salary')) 
      dept =   request.POST.get('dept')
      role = int(request.POST.get('role')) 
      bonus = int(request.POST.get('bonus'))
      phone = int(request.POST.get('phone')) 
      
      new_emp = Employee(first_name=first_name, last_name=last_name, salary=salary,dept_id=dept, role_id = role, hire_date = datetime.now())
      new_emp.save()
      return HttpResponse("Employee added")
    else:
        context = {
            'var':var,
            'rol':rol
        }
    return render(request, 'add_emp.html', context)
#  elif request.method == 'GET':


    # return render(request, 'add_emp.html')

def remove_emp(request, emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id= emp_id)
            emp_to_be_removed.delete()
        except:
            return HttpResponse("Please Enter a valid Emp Id")
    emps = Employee.objects.all()
    context = {
        'emps':emps
    }
    return render(request, 'remove_emp.html',context)

def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            emps = emps.filter(dept__name__icontains = dept)
        if role:
            emps = emps.filter(role__name__icontains = role)
        context = {
            'emps':emps
        }
        return render(request, 'view_all_emp.html', context)
    elif request.method == 'GET':
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse("An Exception Occured")


    return render(request, 'filter_emp.html')



def logout_user(request):
    logout(request)
    return redirect('Signup')


def update(request, id):
    user = Employee.objects.get(id=id)
    de = Department.objects.all()
    rol = Role.objects.all()
    print('id', id)
    if request.method == 'POST':
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.salary = request.POST.get('salary')
        user.dept_id = request.POST['dept']
        user.role_id = request.POST['role']
        user.bonus =request.POST['bonus']
        user.phone = request.POST['phone']
        user.save()
        return redirect('all_emp')
    data = {
        'user':user,
        'de':de,
        'rol':rol
        # 'userr':userr
    }  

    return render(request, 'update.html' , data)