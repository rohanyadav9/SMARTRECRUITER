from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'base.html')
def choice(request):
    a=int(request.POST.get('choice')) 
    if a==1:
        return render(request,'user.html')
    if a==2:
        return render(request,'company.html')
    else:
        return HttpResponse('not valid choice')