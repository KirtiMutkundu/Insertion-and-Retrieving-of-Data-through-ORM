from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *
from django.db.models.functions import Length

def insert_topic(request):
    tn=input('enter topic name')
    TO=Topic.objects.filter(topic_name=tn)
    TO.save()
    d={'QLTO':Topic.objects.all()}
    #return HttpResponse('Topic is created Successfully')
    return render(request,'display_topics.html',d)

def insert_webpage(request):
    tn=input('enter topicname')
    n=input('enter name')
    u=input('enter url')
    e=input('enter email')

   
    LTO=Topic.objects.filter(topic_name=tn)
    if LTO:
        TO=LTO[0]
        WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u,email=e)[0]
        WO.save()
        d={'QLWO':Webpage.objects.all()}
        #return HttpResponse('Webpage is created successfully')
        return render(request,'display_webpages.html',d)
    #else:
        #return HttpRespnse('Given Topic is not present in my Parent Table')

def insert_access(request):
    i=int(input('enter id of webpage object'))
    
    d=input('enter date')
    a=input('enter author') 
    WO=Webpage.objects.get(id=i)
    AO=AccessRecord.objects.get_or_create(name=WO,date=d,author=a)[0]
    AO.save()
    d={'QLAO':Webpage.objects.all()}
    #return HttpResponse('Accessrecord is created successfully')
    return render(request,'display_accessrecord.html',d)


def display_topics(request):
    QLTO=Topic.objects.all()
    d={'QLTO':QLTO}
    return render(request,'display_topics.html',context=d)

def display_webpages(request):
    QLWO=Webpage.objects.all()
    QLWO=Webpage.objects.filter(topic_name='Cricket')
    QLWO=Webpage.objects.exclude(topic_name='Cricket')
    #QLWO=Webpage.objects.get(topic_name='Football') #get() returned more than one Webpage -- it returned 2!
    QLWO=Webpage.objects.all()[ 2:: ]
    QLWO=Webpage.objects.all().order_by('name')
    QLWO=Webpage.objects.all().order_by('-name')
    QLWO=Webpage.objects.all().order_by(Length ('name'))
    QLWO=Webpage.objects.all().order_by(Length ('name').desc())

    QLWO=Webpage.objects.filter(name__startswith='m')
    QLWO=Webpage.objects.filter(name__endswith='o')
    QLWO=Webpage.objects.filter(name__contains='d')
    QLWO=Webpage.objects.filter(url__contains='l')
    QLWO=Webpage.objects.filter(name__in=['msd'])
    QLWO=Webpage.objects.filter(name__in=['msd','Virat']) #case sensitive

    d={'QLWO':QLWO}
    return render(request,'display_webpages.html', d)

def display_accessrecord(request):
    QLAO=AccessRecord.objects.all()
    #QLAO=AccessRecord.objects.all

    QLAO=AccessRecord.objects.filter(date='2004-08-25')
    QLAO=AccessRecord.objects.filter(date__year='2000')
    QLAO=AccessRecord.objects.filter(date__month='7')
    QLAO=AccessRecord.objects.filter(date__day='26')
    QLAO=AccessRecord.objects.filter(date__gt='2004-08-25')
    QLAO=AccessRecord.objects.filter(date__lte='2023-08-25')
    QLAO=AccessRecord.objects.filter(date__year__gt='2023')


    d={'QLAO':QLAO}
    return render(request,'display_accessrecord.html', d)
    
