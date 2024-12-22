from django.shortcuts import render,HttpResponseRedirect
from .models import Post
from .forms import SignUpForm,LoginForm,PostForm
from django.contrib.auth import login,authenticate,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.models import Group
# Create your views here.

# HomePage
def Home(request):
    post = Post.objects.all()
    return render(request,"blog/home.html",{"post":post})

# AboutPage
def About(request):
    return render(request,"blog/about.html")

# ContactPage
def Contact(request):
    return render(request,"blog/contact.html")

# dashboardPage
def Dashboard(request):
    if request.user.is_authenticated:
        post = Post.objects.all()
        user = request.user
        # gps = user.groups.all()
        return render(request,"blog/dashboard.html",{"post":post,"full_name":user})
    
    else:
        return HttpResponseRedirect("/")

# logoutPage
def User_Logout(request):
    logout(request)
    return HttpResponseRedirect("/")

# SignupPage
def Signuppage(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            group=Group.objects.get(name="Author")
            user.groups.add(group)
            form = SignUpForm()
            messages.success(request,"Register Successfully !! ")
    else:
        form = SignUpForm()
    return render(request,"blog/signup.html",{"form":form})

# LoginPage
def Loginpage(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            form = LoginForm(request=request,data=request.POST)
            if form.is_valid():
                v_user = form.cleaned_data["username"]
                v_pass = form.cleaned_data["password"]
                auth = authenticate(username = v_user,password= v_pass)
                if auth is not None:
                    login(request,auth)
                    messages.success(request,"Logged In Successfully !!")
                    return HttpResponseRedirect("/dashboard/")
        else:
            form = LoginForm()
        return render(request,"blog/login.html",{"form":form})
    else:
        return HttpResponseRedirect("/dashboard/")

# Add New Post
def add_post(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                valid_title = form.cleaned_data["title"]
                valid_desc = form.cleaned_data["desc"]
                pst = Post(title = valid_title, desc = valid_desc)
                pst.save()
                form = PostForm
                messages.success(request,"Your Post successfully Added....")
                return HttpResponseRedirect("/dashboard/")
        else:
            form = PostForm()
        return render(request,"blog/addpost.html",{"form":form})
    else:
        return HttpResponseRedirect("/login/")
     
# Update Post
def update_post(request,id):
    if request.user.is_authenticated:
        if request.method=="POST":
            pi = Post.objects.get(pk=id)
            form = PostForm(request.POST,instance=pi)
            if form.is_valid():
                form.save()
                messages.success(request,"Post Updated Successfully !!")
                return HttpResponseRedirect("/dashboard/")
        else:
            pi = Post.objects.get(pk=id)
            form = PostForm(instance=pi)
        return render(request,"blog/updatepost.html",{"form":form})
    else:
        return HttpResponseRedirect("/login/")
# delete Post
def delete_post(request,id):
    if request.user.is_authenticated:
        d_data = Post.objects.get(pk=id)
        d_data.delete()
        messages.success(request,"Post Deleted Successfully !!")
        return HttpResponseRedirect("/dashboard/")
    else:
        return HttpResponseRedirect("/login/")