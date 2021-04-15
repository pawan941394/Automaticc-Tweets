from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator

from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.db.models import Q
from django.views.generic.edit import UpdateView,CreateView
from django.http.response import HttpResponseRedirect
from django.views.generic import TemplateView
from django.http import HttpResponse
# Create your views here.


from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Contact, Tweet, Category
from datetime import date



class HomeView(TemplateView):
    template_name = 'website/home.html'


class BlogListView(TemplateView):
    template_name = 'website/blog-list.html'

class BlogDetailView(TemplateView):
    template_name = 'website/blog_details.html'

def logIn(request):
    if request.method =='POST':
        loginusername = request.POST['username']
        loginpassword = request.POST['password']

        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return redirect('login')
    return render(request, 'website/login_form.html')

def signUp(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        phone = request.POST['phone']
        username = request.POST['username']
        password = request.POST['password']
        cPassword = request.POST['cPassword']
        database = User.objects.filter(username=username).exists()
        if password==cPassword and  database==False :
            myuser = User.objects.create_user(username, password)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.phone_no = phone
            myuser.save()
            return redirect("login")
        return redirect('register')
    return render(request, 'website/register_form.html')

def handlelogout(request):
    logout(request)
    return redirect('/')

def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']       
        phone = request.POST['phone']
        message = request.POST['message']
        contact = Contact(name=name, email=email, subject=subject, phone=phone, message=message)
        contact.save()
        return redirect('contact')

    return render(request, 'website/contact.html')

def tweets(request):
    categories = Category.objects.all()
    context = {
        'categories':categories
    }
    return render(request, 'website/cat.html', context=context)

def tweetPost(request, slug):
    category = Category.objects.filter(slug=slug)
    allTweets = Tweet.objects.filter(category__in=category)
    context = {
        'tweets':allTweets,
        'today' : date.today(),
    }
    return render(request, 'website/blog-list.html', context=context)

def tweetPostDetail(request, slug):
    tweet_detail = Tweet.objects.get(slug=slug)
    context = {
        'tweet': tweet_detail
    }
    return render(request, 'website/blog_details.html', context=context)

def about(request):
    return render(request, 'website/about.html')
