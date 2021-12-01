from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm,forms,AuthenticationForm
#from django.contrib.auth.models import  User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from . import scraper
#
def index(request):
    """
    This is main page.
    """
    if request.user.is_authenticated:
        return render(request,'scraper/index.html')
    else:
        return HttpResponseRedirect('/scraper/signup/')

def validate(request):
    """
    This function will validate the details filled in forms.
    """
    try:
        if request.user.is_authenticated:
            if request.method=='POST':
                name=request.POST['search_item']
                category=request.POST['options']
                number=request.POST['number']

                obj=scraper.Searching(name,category,number)
                data,filename=obj.too_csv()
                data_dict={'data':data[1:]}
                arguments={'data':data_dict,'columns':data[0],'filename':filename,'header':name}
                return render(request,'scraper/basic.html',arguments)
        else:
            return HttpResponseRedirect('/scraper/login/')
    except Exception as e:
        return e

def signup(request):
    """
    This is signup form
    """

    password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput)
    if request.method == 'POST':
        fm=UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
            #messages.success(request,"Your registration successful.")
            return HttpResponseRedirect('/scraper/login/')

    else:
        fm=UserCreationForm()
    return render(request,'scraper/signup.html',{'form':fm})

def user_login(request):
    """
    This is login function
    """
    if not request.user.is_authenticated:
        if request.method == 'POST':
             fm=AuthenticationForm(request=request,data=request.POST)
             if fm.is_valid():
                 username=fm.cleaned_data['username']
                 password=fm.cleaned_data['password']
                 user=authenticate(request,username=username,password=password)
                 if user is not None:
                     login(request,user)
                     messages.success(request,"You logged in successfully.")
                     return HttpResponseRedirect('/scraper/')
        else:
            fm=AuthenticationForm()
        return render(request,'scraper/login.html',{'form':fm})
    else:
        return HttpResponseRedirect('/scraper/')
def user_logout(request):
    if request.user.is_authenticated:
         logout(request)
         return HttpResponseRedirect('/scraper/login/')
