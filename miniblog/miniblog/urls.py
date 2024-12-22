"""
URL configuration for miniblog project.

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
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.Home,name="home"),
    path("about/",views.About,name="about"),
    path("contact/",views.Contact,name="contact"),
    path("dashboard/",views.Dashboard,name="dashboard"),
    path("logout/",views.User_Logout,name="logout"),
    path("login/",views.Loginpage,name="login"),
    path("signup/",views.Signuppage,name="signup"), 
    path("update/<int:id>",views.update_post,name="update"),
    path("add/",views.add_post,name="add"),
    path("delete/<int:id>",views.delete_post,name="delete"),
]
