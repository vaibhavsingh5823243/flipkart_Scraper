from django.shortcuts import render,HttpResponseRedirect
def index(request):
    if request.user.is_authenticated:
        return render(request,'index.html')
    else:
        return HttpResponseRedirect('/scraper/signup/')