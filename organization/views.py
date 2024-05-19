from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import organization
from .models import emp_detail
from employe.models import details


def sign_com(request):
    b=request.POST.get('sign_com')
    if b=='login':
        return render(request,'com_in.html')
    if b=='logup':
        return render(request,'com_up.html')
         
def login(request):
    if request.method == 'POST':
       username = request.POST.get('username')
       password = request.POST.get('password')
       com_instance = organization.objects.filter(username=username).first()
       if com_instance and com_instance.password==password:
           request.session['username'] = username
           return redirect('com_details')
       else:
           return HttpResponse('Invalid username or password')  
   
def logup(request):
    if request.method=='POST':
            com_name=request.POST['com_name']
            username=request.POST['username']
            password=request.POST['password']
            post=request.POST['post']
            experience=request.POST['experience']
            language=request.POST['language']
            skills=request.POST['skills']
            qualification=request.POST['qualification']
            about=request.POST['about']
            if organization.objects.filter(username=username).exists():
                return HttpResponse('username is taken')
            else:
                a=organization(com_name=com_name,username=username,password=password,about=about,qualification=qualification,experience=experience,language=language,post=post,skills=skills)      
                a.save()
                request.session['username'] = username
                return render(request,'emp.html')
            
def emp(request):
    if request.method=='POST':
        username=request.session.get('username')
        d=organization.objects.filter(username=username).first()
        e=d.com_name
        for i in range(10):
            name=request.POST.get('name{}'.format(i))
            post=request.POST.get('post{}'.format(i))
            profile=request.POST.get('profile{}'.format(i))
            if name and post and profile:
               a=emp_detail(name=name,post=post,profile=profile,company=e)
               a.save()
        return redirect('com_details')
    

def com_details(request):
    username = request.session.get('username')
    d=organization.objects.filter(username=username).first()
    e=d.com_name
    c=details.objects.filter(company=e).values_list('name','qualification','skills','experience','personal_skills','email','phone')
    if not c:
        return HttpResponse('u dont have any candidate')
    else:
        return render(request,'com_details.html',{'name':e,'c':c})