from django.shortcuts import render, redirect
from django.http import request
from .models import Post
from datetime import datetime

#Django Contrib libraries for user login and sign up
from django.contrib.auth.models import User, auth, Group
from django.contrib import messages

# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def post(request, pk):
    posts = Post.objects.get(id=pk)
    return render(request, 'posts.html', {'posts': posts})

def add_post(request):
    if request.method == 'POST':
        author = request.user
        if(request.user.is_authenticated):
            title = request.POST['title']
            body = request.POST['body']
            # created_at = datetime.now()
            new_post = Post.objects.create(author=author, title = title, body = body)
            new_post.save()
            post_id = new_post.id
            return redirect('/post/'+str(post_id))
        else:
            messages.info(request, "Not authenticated to add posts")
            return redirect('add_post')
    else:
        return render(request, 'add_post.html')

def profile(request, uid):
    posts = Post.objects.filter(author_id=uid)
    username = User.objects.get(id=uid)
    return render(request, 'profiles.html', {'posts': posts, 'username': username})#, {'posts': posts})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email is already in use!")
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username is already in use!")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email = email, password= password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, "Password and Retyped password are not the same!")
            return redirect('register')
    else:
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')