from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from rest_framework import renderers
from .forms import FormClass
from .models import Model
from .serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.http import HttpResponseRedirect


# Create your views here.

def validation(request):
    return render (request,'./base.html')

def thankyou(request):
    return render(request,'success.html')

def ShowFormData(request):
    if request.method == "POST":
        fm=FormClass(request.POST, auto_id="some_%s",label_suffix='--',initial={'Name':'santosh','Email':'Email'})
        if fm.is_valid():
            print('ye post method se aaya hai')
            print("from validation")
            name=fm.cleaned_data['Name']
            age=fm.cleaned_data['Age']
            email=fm.cleaned_data['Email']
            place=fm.cleaned_data['Place']
            psd=fm.cleaned_data['Password']
            re_psd=fm.cleaned_data['ReEnterPassword']

            #SAVE DATA TO MODEL
            reg=Model(Name=name,Age=age,Email=email,Place=place,Password=psd,ReEnterPassword=re_psd)
            reg.save()

            print("Name:",name)
            print('Age:',age)
            print('Email:',email)
            print('Place:',place)            
            print('Password:',psd)
            print('Re_Enter_Password:',re_psd)
            # if psd != re_psd:
            #     print('password error')
            #     wrong='wrong password'
            #     return render (request,'form.html',{'data':fm,'nm':name,'wrg':wrong})

            # else:
            #     print('password match')
            #     wrong='right password'
            #     return render (request,'base.html',{'nm':name,'wrg':wrong})
            # Write = psd != re_psd
            # if Write :
            #     print('password error')
            #     wrong='wrong password'

            # else:
            #     print('password match')
            #     wrong='right password'
            return HttpResponseRedirect('/blog/success/')
            # ,{'wrt':wrong}

    else:
        fm=FormClass()  
        print('ye get method se aaya hai')
    return render (request,'form.html',{'data':fm,})


def student_detail(request,inp):
    stu=Model.objects.get(pk=inp)
    serializer=StudentSerializers(stu)
    json_data=JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')

def student_detail1(request):
    stu=Model.objects.all()
    serializer=StudentSerializers(stu,many=True)
    json_data=JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')