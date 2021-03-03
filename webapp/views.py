from django.shortcuts import render, redirect
from .models import Blog
from django.contrib.auth.admin import User
from django.contrib.auth.decorators import login_required
from .forms import Register_form, Blog_Form
from django.contrib.auth import authenticate, login

@login_required
def index(request):

    username = None
    data = Blog.objects.all()

    try:
        username = User.objects.get(username=request.user.username)
    except User.DoesNotExist:
        return render(request, 'webapp/index.html', {'data': data,'username':username})


    return render(request, 'webapp/index.html', {'data':data, 'username':username})

@login_required
def Blog_Post(request):

    if request.method == 'POST':
        form = Blog_Form(request.POST)
        form.instance.author = request.user
        if form.is_valid():
            fs = form.save(commit=False)
            fs.user = request.user
            fs.save()
            return redirect('main')
    else:
        form =Blog_Form()
    return render(request, 'webapp/blog.html',{'form':form})


def registration(request):

    if request.method == 'POST':
        form = Register_form(data=request.POST)
        if form.is_valid():
            user1 = form.save(commit=False)
            user1.set_password(user1.password)
            user1.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')



            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect('main')
    else:
        form = Register_form()
    return render(request,'webapp/register.html',{'form':form})


