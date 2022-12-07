from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'home.html')

def blogs_list(request):
    all_blogs = Blog.objects.all()
    context = {}
    context['all_blogs'] = all_blogs
    return render(request, 'blogs_list.html', context)

def blog_view(request, id):
    particular_blog = Blog.objects.get(id = id)
    print(particular_blog.id)
    context={"blog":particular_blog}
    
    return render(request, 'blog.html',context)

def guest_blogs_list(request):
        return render(request, 'home.html')

def about_blog(request):
    return render(request, 'about_blog.html')

def about_me(request):
    return render(request, 'about_me.html')

def subscriber_page(request):
    if request.method == 'POST':
        name = request.POST['fname']
        email = request.POST['email']
        num = request.POST['number']
        instance = Subscriber(name=name, email=email, number=num)
        instance.save()
        return redirect('home')
    return render(request, 'subscriber.html')