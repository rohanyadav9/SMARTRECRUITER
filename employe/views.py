from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import employe
from .models import details
from organization.models import organization
from organization.models import emp_detail
from django.core.mail import send_mail
from django.conf import settings


    
def signin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        a=employe.objects.filter(username=username).first()
        if a and a.password==password:
            request.session['username'] = username
            return redirect('matching')
        else:
            return HttpResponse('invalid username')
            
    else:
        return render(request,'b.html')



def signup(request):
    if request.method=='POST':
        name=request.POST['name']
        username=request.POST['username']
        password=request.POST['password']
        qualification=request.POST['qualification']
        skills=request.POST['skills']
        language=request.POST['language']
        personal_skills=request.POST['personal_skills']
        experience=request.POST['experience']
        email=request.POST['email']
        phone=request.POST['phone']
        if employe.objects.filter(username=username).exists():
                return HttpResponse('username is taken')

        a=employe(name=name,username=username,password=password,qualification=qualification,skills=skills,language=language,personal_skills=personal_skills,experience=experience,email=email,phone=phone)
        a.save()
        request.session['username'] = username
        return redirect('matching')
    else:
        return render(request,'r.html')
 


def matching(request):
   
    if request.method == 'POST':
        com_name = request.POST.get('name')
        username = request.session.get('username')
        e=organization.objects.filter(com_name=com_name).first()
        d=employe.objects.filter(username=username).first()
        marks=0
        sk=['communication','interpersonal','teamwork','workaholic','problem solving','adaptibility','time management','leadership','emotional intelligence','creative','networking','attention to detail','self-motivation','cultural sensitivity']
        st=['python','django','java','oops','node.js','reacts.js','ai','ml','html','css','javascript','pandas','matplotib','numpy','mongo.db','postgresql','sql','nosql','c++','c#','c']
        for a in d.qualification:
            if a in e.qualification:
               marks+=1
            elif a not in e.qualification:
                marks+=0
        
        for a in d.language:
           if a in e.language:
               marks+=0.5
           elif a not in e.language:
               marks+=0
        
        for skill in d.personal_skills:
            if skill in sk:
                marks += 0.5
            elif skill not in sk:
                marks+=0
       
        
        for skill in e.skills:
            if skill in st:
                st.remove(skill)
        
            for skill in d.skills:
                if skill in st:
                  marks += 1
                elif skill not in st:
                    marks+=0
       
        if d.experience>=e.experience:
            marks+=1
        elif d.experience<e.experience:
            marks+=0
        

        if marks>0:
            name=d.name
            qualification=d.qualification
            skills=d.skills
            personal_skills=d.personal_skills
            email=d.email
            phone=d.phone
            experience=d.experience
            company=e.com_name
            x=details(name=name,qualification=qualification,experience=experience,skills=skills,personal_skills=personal_skills,email=email,phone=phone,company=company)
            x.save()
            request.session['email'] = email
            request.session['name'] = name
            request.session['com_name'] = com_name
            return redirect('send_email')

    else:
        username = request.session.get('username')
        d=employe.objects.filter(username=username).first()
        e=d.name
        c=organization.objects.values_list('com_name','post','about')
        return render(request,'f.html',{'name':e,'c':c})
 
      


def send_email(request):
    a=request.session.get('email')
    b=request.session.get('name')
    c=request.session.get('com_name')
    d=emp_detail.objects.filter(company=c).all()
    e=''
    for employe in d:
        e+=f"name : {employe.name}, post : {employe.post}, linkdin profile : {employe.profile}\n"
    subject = 'MAIL REGARDING RESUME SHORTLISTING'
    message = f'''Heloo,{b}

     This mail is regarding to inform you ,that you, fullfilled the requirement of the {c} in which you applied through our website.
    
     
     The company will contact you shortly.In the mean time you can contact {c}'s employe.
     
     Employe Details:
     {e}

     Thank you 
     Regards
     SMARTRECRUITER
     
     '''
    from_email = settings.EMAIL_HOST_USER  
    to_email = [a]
    send_mail(subject, message, from_email, to_email)
    return HttpResponse("thanku")
