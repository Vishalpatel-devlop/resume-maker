from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse 
from resume_maker.models import *
from django.shortcuts import redirect, render
def personal(request):
    if request.method=="POST":
        first=request.POST.get('first_name') # here first is variable and first_name is name of input in the html page.
        last=request.POST.get('last_name')
        contact=request.POST.get('contact')
        mail=request.POST.get('mail')
        location=request.POST.get('location')
        linkedin=request.POST.get('LinkedIn')
        obj=request.POST.get('objective')
        dob=request.POST.get('d.o.b')
        per=get_data1(first_name=first,last_name=last,linkedin=linkedin,contact=contact,email=mail,location=location,dob=dob,objective=obj) # here first_name is model's variable and first is variable which is used here.
        per.save()# ^ get_data1 is model's name and per is variable.
        return redirect('skill')
    return render(request, "resume_page1.html") 


def skill(request):
    if request.method=="POST":
        hard=request.POST.get('hard')
        soft=request.POST.get('soft')
        a = get_data1.objects.last()
        skills=get_data2(hard_skill=hard,soft_skill=soft,person_id=a)
        skills.save()
        return redirect('ug_pg')
    return render(request, "resume_page2.html")    

def edu(request):
    if request.method=="POST":
        inst_name=request.POST.get('inst_name')
        loc=request.POST.get('location')
        degree=request.POST.get('degree')
        date=request.POST.get('date')
        a = get_data1.objects.last()
        edu_info=get_data3(inst_name=inst_name,degree_name=degree,location=loc,g_date=date,person_id=a)
        edu_info.save()
        return redirect('edu2')
    return render(request, "resume_page3.html")    


def exp(request):
    if request.method=="POST":
        job=request.POST.get('job')
        cname=request.POST.get('cname')
        achieve=request.POST.get('achieve')
        jdate=request.POST.get('jdate')
        tdate=request.POST.get('tdate')
        a = get_data1.objects.last()
        exp=get_data4(job_title=job,comp_name=cname,doj=jdate,dol=tdate,achievement=achieve,person_id=a)
        exp.save()
        return redirect('other')
    return render(request, "resume_page4.html")    



def other(request):
    if request.method=="POST":
        hobby=request.POST.get('hobby')
        ability=request.POST.get('ability')
        certi=request.POST.get('certi')
        project=request.POST.get('project')
        img=request.FILES.get("image")
        a = get_data1.objects.last()
        other_info=get_data5(projects=project,ability=ability,hobby=hobby,certificate=certi,img=img,person_id=a)
        other_info.save()
        return redirect('resumemaker')
    return render(request, "resume_page5.html")    


def edu2(request):
    if request.method=="POST":
        sname=request.POST.get('sname')
        loc=request.POST.get('loc')
        per10=request.POST.get('per10')
        per12=request.POST.get('per12')
        a = get_data1.objects.last()
        edu2_info=get_data6(school=sname,location=loc,percent_10=per10,percent_12=per12,person_id=a)
        edu2_info.save()
        return redirect('expornot')
    return render(request, "resume_page6.html")    

def resumemaker(request):
   a = get_data1.objects.last()
   b = get_data2.objects.filter(person_id=a.id)
   c = get_data3.objects.filter(person_id=a.id)
   d = get_data4.objects.filter(person_id=a.id)
   e = get_data5.objects.filter(person_id=a.id)
   f = get_data6.objects.filter(person_id=a.id)
   datas={
      'a':a,
      're1':b,
      're2':c,
      're3':d,
      're4':e,
      're5':f,

         }  
   return render(request,"AI_resume.html",datas)

def ug(request):
    if request.method=="GET":
      return redirect('edu2')
    return render(request, "ug_pg.html")  

def pg(request):
    if request.method=="GET":
      return redirect('edu')

    return render(request, "ug_pg.html")  

def ug_pg(request):
    if request.method=='GET':
        return render(request,"ug_pg.html")
    

def expornot(request):
    if request.method=="GET":
     return render(request, "exp_or_not.html")  

def yes_exp(request):
    if request.method=="GET":
      return redirect('exp')

    return render(request, "exp_or_not.html")  

def no_exp(request):
    if request.method=='GET':
         return redirect('other')
    return render(request,"exp_or_not.html")    