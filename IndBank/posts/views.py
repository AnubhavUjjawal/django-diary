from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate, login , logout
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required



# Create your views here.
@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            print (username,password)
            user = authenticate(username=username,password=password)
            print(user)
            login(request,user)
            return HttpResponseRedirect(reverse('posts:homepage',kwargs={'username':user.username}))
            #return HttpResponse("hello")
        except Exception:
            return HttpResponseRedirect(reverse('posts:login_page'))
@csrf_exempt
def add_user(request):
    if request.user.is_authenticated:
        print(request.user.email)
        return render(request,'posts/main.html')
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request,new_user)
            # redirect, or however you want to get to the main view
            return HttpResponseRedirect(reverse('posts:homepage',kwargs={'username':request.user.username}))
    else:
        form = UserForm() 

    return render(request, 'posts/adduser.html', {'form': form}) 

def add_post(request):
    if not request.user.is_authenticated:
        return render(request,'posts/main.html',context={'error':'not loggedin'})
    form = PostForm(request.GET)
    if form.is_valid():
        x = form.cleaned_data
        x['author'] = request.user
        new_post = Posts.create(x)
        new_post.save()
        return HttpResponseRedirect(reverse('posts:homepage',kwargs={'username':request.user.username}))
        #return render(request,'posts/main.html')
    else:
        #return render(request,'posts/main.html',{'error':'posterror'})
        return HttpResponseRedirect(reverse('posts:homepage',kwargs={'username':request.user.username,'error':'posterror'}))

def user_logout(request):
    logout(request)
    return render(request,'posts/index.html')

def login_page(request):
    return render(request,'posts/index.html')
@login_required
def homepage(request,username):
    user = User.objects.get(username=username)
    cxt = {'user':user
}
    return render(request,'posts/user.html',cxt)

def profile(request,username):
    user = User.objects.get(username=username)
    cxt = {'user':user
}
    return render(request,'posts/user_profile.html',cxt)

