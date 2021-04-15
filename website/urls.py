from django.contrib import admin
from django.urls import path
from django.urls.conf import include, path
from django.views.generic.base import RedirectView
from website import views

urlpatterns = [
   path('',views.HomeView.as_view()),
   path('about',views.about, name='about'),
   path('contact',views.contact, name='contact'),
   path('register',views.signUp, name='signUp'),
   path('tweets',views.tweets, name='tweets'),
   path('tweets/<str:slug>', views.tweetPost, name='tweetPost'),
   path('tweets/tweet/<str:slug>', views.tweetPostDetail, name='tweetPostDetail'),
   path('login',views.logIn, name='login'),
   path('blog_list',views.BlogListView.as_view()),
   path('logout',views.handlelogout, name='logout'),
   path('blog_details',views.BlogDetailView.as_view()),
   # path('contact/',views.ContactView.as_view()),
   # path('accounts/', include('registration.backends.default.urls')),
   # path('profile/edit/<int:pk>',views.MYProfileUpdateView.as_view(success_url = '/social/home')),
   # path('mypost/create/', views.MYPostCreate.as_view(success_url="/social/home")),
   #
]
