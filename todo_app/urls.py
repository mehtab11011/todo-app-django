"""
URL configuration for todo_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todo_app import views

urlpatterns = [
    
     path('admin/', admin.site.urls),
    path('', views.login,name="login_page"),
    path('register_page/', views.register_page,name="register_page"),
    path("home_page/",views.home_page,name="home_page"),
    path("add_task/",views.addtask_f,name="add_task"),
    path("task_list/",views.tasklist,name="task_list"),
    path('edit_task/<int:id>/',views.edittask, name='edit_task'),  
    path("task_details",views.taskdetail,name="task_details"),
    path("profile_page",views.profilepage,name="profile_page"),
    path('delete_task/<int:id>/', views.deletetask, name='delete_task'),

]

   
    
