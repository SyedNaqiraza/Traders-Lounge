from django.shortcuts import render
from django.views import generic
from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from .models import registration
from .models import Company
from .models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

class index(generic.ListView):
    template_name = 'logintemplate/landing.html'
    queryset = ''

def methodology(request):
    return render(request, "logintemplate/methodology.html")

def signup(request):
    form=UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, "logintemplate/signup.html", {'form':form})

@login_required
def homepage(request):
    USER=registration.objects.filter(users=request.user.id)
    args={'users':USER}
    return render(request,'Mainpage/companies.html',args)
def subscribe(request):
    user='subs'
    company1=request.POST.get("option")
    if company1 :
        use=User.objects.get(id=request.user.id)
        com=Company(CompanyName='Apple')
        dat=registration()
        dat.users=use
        dat.company=com
        dat.save()
        USER = registration.objects.filter(users=request.user.id)
        args = {'users': USER}
        return render(request,'Mainpage/companies.html',args)
    args = {'sub': user,'comp':company1}
    return render(request, 'Mainpage/companies.html',args)