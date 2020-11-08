from django.conf.urls import url,include
from django.contrib.auth import views as auth_views
from . import views
from django.urls import path, include
from django.conf import settings

urlpatterns = [
url(r'^$', views.index.as_view(), name='home'),
url(r'^signup/$', views.signup, name='signup'),
path('homepage/', views.homepage, name='homepage'),
path('homepage/subscribe', views.subscribe, name='subs'),
path('methodology', views.methodology, name='method'),
path('log/', auth_views.LoginView.as_view(template_name='logintemplate/login.html'), name='login'),
path('logout/', auth_views.LogoutView.as_view(template_name='logintemplate/landing.html'), name='logout'),
]