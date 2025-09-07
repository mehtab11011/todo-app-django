from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from registration.models import register
from addtask.models import TaskAddModel
from django.contrib.auth.hashers import make_password


def home_page(request):
    username = request.session.get("username", "guest")
    return render(request, "home_page.html", {"username": username})


def login(request):
  if request.method == "POST":
    login_email = request.POST.get("email")
    login_password = request.POST.get("password")

    user = register.objects.filter(email=login_email, password=login_password).first()

    if user:
        request.session['username'] = user.username
        request.session["email"] = user.email
        return redirect("home_page")
    else:
        return render(request, "login_page.html", {"error": "Invalid email and password"})
  else:  
    return render(request, "login_page.html")

def register_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        data_save = register(username=username, email=email, password=password)
        data_save.save()
        return redirect("login_page")

    data = {
        "data_get": register.objects.all(),
    }
    return render(request, "register_page.html", data)


from datetime import datetime

def addtask_f(request):
    task_data = TaskAddModel.objects.all()
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        date_str = request.POST.get("date")
        priority = request.POST.get("priority")

        # Convert string to Python date object
        date = datetime.strptime(date_str, "%Y-%m-%d").date() if date_str else None

        data_save = TaskAddModel(
            name=name,
            description=description,
            date=date,
            priority=priority
        )
        data_save.save()
        return redirect("task_list")

    return render(request, "add_task.html", {"task_data": task_data})



def tasklist(request):
    view_data = TaskAddModel.objects.all()
    data = {
        "view_data": view_data
    }
    return render(request, "task_list.html", data)


def edittask(request, id):
    task = get_object_or_404(TaskAddModel, id=id)

    if request.method == "POST":
        task.name = request.POST.get("task_name")
        task.description = request.POST.get("description")
        date_str = request.POST.get("date")
        task.date = datetime.strptime(date_str, "%Y-%m-%d").date() if date_str else None
        task.priority = request.POST.get("priority")
        task.save()
        return redirect('task_list')

    return render(request, "edit_task.html", {"task": task})



def taskdetail(request):
    detail_data = TaskAddModel.objects.all()
    data = {
        "detail_data": detail_data
    }
    return render(request, "task_details.html", data)


def profilepage(request):
    # Get current user info from session
    username = request.session.get("username", "guest")
    email = request.session.get("email", "guest111@gmail.com")

    if request.method == 'POST':
        username_up = request.POST.get("username")
        email_up = request.POST.get("email")
        password_up = request.POST.get("password")    

        # Find the current user
        user = register.objects.filter(email=email).first()

        if user:
            user.username = username_up 
            user.email = email_up 
            
            if password_up: 
                user.password = make_password(password_up) 
            
            user.save()  

            
            request.session['username'] = username_up
            request.session['email'] = email_up
            
            return redirect("home_page")
    

    return render(request, "profile_page.html", {
        "username": username,
        "email": email
    })

def deletetask(request, id):
    task = get_object_or_404(TaskAddModel, id=id)
    task.delete()
    return redirect('task_list')
