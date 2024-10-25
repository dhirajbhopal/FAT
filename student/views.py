from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.shortcuts import render , redirect
from django.http import HttpResponse
from student.models import fat
from student.models import donation
from django.contrib.auth.models import User
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from random import randint
from django.shortcuts import render
from django.conf import settings
import time
import qrcode
from PIL import Image
from io import BytesIO
import base64
from django.core.files.uploadedfile import InMemoryUploadedFile
import pyqrcode
import png
from django.urls import reverse
from pyqrcode import QRCode
import tkinter as tk
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from django.contrib.auth.signals import user_logged_out, user_logged_in
from django.contrib.auth import logout
from django.views.decorators.cache import cache_control
from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.auth import logout
from django.core.cache import cache


"""def insert(req):
    email=req.GET.get("email")
    passs=req.GET.get("password")
    user = authenticate(req, username=email, password=passs)
    if user is not None:
        userdetail=User.objects.filter(username=email)
        fatall=fat.objects.all()
        return render(req,'insert.html',{'userdetail':userdetail,'fatall':fatall,'passs':passs})
    else:
        messages.error(req,'Invalid Username Or Password')
        return redirect('/')
    return redirect('/')"""

def insert(req):
    email=req.GET.get("email")
    userdetail=User.objects.filter(username=email)
    for i in userdetail:
        emailid=i.username
        if (email==emailid):
            userdetail=User.objects.filter(username=email)
            fatall=fat.objects.all()
            return render(req,'insert.html',{'userdetail':userdetail,'fatall':fatall})
        else:
            messages.error(req,'You are not Loggedin')
            return redirect('/')
    return redirect('/')

def donate(req):
    email=req.GET.get("email")
    userdetail=User.objects.filter(username=email)
    for i in userdetail:
        emailid=i.username
        if (email==emailid):
            userdetail=User.objects.filter(username=email)
            return render(req,'donate.html',{'userdetail':userdetail})
        else:
            messages.error(req,'You are not Loggedin')
            return redirect('/')
    return redirect('/')

def logins(request):
    return render(request,'login.html')

def edit(req):
    email=req.GET.get("email")
    userdetail=User.objects.filter(username=email)
    for i in userdetail:
        emailid=i.username
        if (email==emailid):
            userdetail=User.objects.filter(username=email)
            return render(req,'edits.html',{'userdetail':userdetail})
        else:
            messages.error(req,'You are not Loggedin')
            return redirect('/')
    return redirect('/')

def all(req):
    email=req.GET.get("email")
    userdetail=User.objects.filter(username=email)
    for i in userdetail:
        emailid=i.username
        if (email==emailid):
            userdetail=User.objects.filter(username=email)
            fatall=fat.objects.all()
            return render(req,'fatall.html',{'userdetail':userdetail,'fatall':fatall})
        else:
            messages.error(req,'You are not Loggedin')
            return redirect('/')
    return redirect('/')

def insertqr(req):
    email=req.GET.get("email")
    userdetail=User.objects.filter(username=email)
    for i in userdetail:
        emailid=i.username
        if (email==emailid):
            userdetail=User.objects.filter(username=email)
            return render(req,'qrupdate.html',{'userdetail':userdetail})
        else:
            messages.error(req,'You are not Loggedin')
            return redirect('/')
    return redirect('/')

def newphoto(req):
    email=req.GET.get("email")
    userdetail=User.objects.filter(username=email)
    for i in userdetail:
        emailid=i.username
        if (email==emailid):
            userdetail=User.objects.filter(username=email)
            return render(req,'updatephoto.html',{'userdetail':userdetail})
        else:
            messages.error(req,'You are not Loggedin')
            return redirect('/')
    return redirect('/')

def upload(req):
    email=req.GET.get("email")
    userdetail=User.objects.filter(username=email)
    for i in userdetail:
        emailid=i.username
        if (email==emailid):
            userdetail=User.objects.filter(username=email)
            fatdata=fat.objects.filter(status="raw")
            return render(req,'upload.html',{'userdetail':userdetail,'fatdata':fatdata})
        else:
            messages.error(req,'You are not Loggedin')
            return redirect('/')
    return redirect('/')

def empfatdata(request):
    ob=fat()
    ob.name=request.POST.get("name")
    ob.empid=request.POST.get("empid")
    ob.dept=request.POST.get("dept")
    ob.circle=request.POST.get("circle")
    ob.location=request.POST.get("location")
    ob.grade=request.POST.get("grade")
    ob.date=request.POST.get("date")
    ob.certno=request.POST.get("certno")
    ob.image=request.FILES['image']
    ob.save()
    return HttpResponse("Data Saved")

def updateqr(req):
    empid=req.POST.get("empid")
    qrlinks=req.POST.get("qrlink")
    nqr=fat.objects.get(empid=empid)
    nqr.status="Done"
    nqr.qrlink=qrlinks
    nqr.save()
    return HttpResponse("New QR Link Updated")

def updatephoto(req):
    empid=req.POST.get("empid")
    nqr=fat.objects.get(empid=empid)
    nqr.image=req.FILES['image']
    nqr.save()
    return HttpResponse("New Photo Updated")

def editdata(request):
    if request.method=="GET":
        empid=request.GET.get("empid")
        edits=fat.objects.get(empid=empid)
        edits=fat.objects.filter(empid=empid)
        return render(request,'edit2.html',{'edits':edits,})
    else:
        empid=request.GET.get("empid")
        edits2=fat.objects.get(empid=empid)
        edits2.name=request.POST.get("name")
        edits2.dept=request.POST.get("dept")
        edits2.circle=request.POST.get("circle")
        edits2.location=request.POST.get("location")
        edits2.grade=request.POST.get("grade")
        edits2.date=request.POST.get("date")
        edits2.certno=request.POST.get("certno")
        edits2.status="raw"
        edits2.save()
        return HttpResponse("Data Saved")
    return redirect('/')

"""def editdata(request):
    if request.method=="GET":
        email=request.GET.get("email")
        empid=request.GET.get("empid")
        userdetail=User.objects.filter(username=email)
        for i in userdetail:
            emailid=i.username
            if (email==emailid):
                edits=fat.objects.get(empid=empid)
                edits=fat.objects.filter(empid=empid)
                userdetail=User.objects.filter(username=email)
                return render(request,'edit2.html',{'edits':edits,'userdetail':userdetail})
            else:
                messages.error(req,'You are not Loggedin')
                return redirect('/')
    else:
        empid=request.GET.get("empid")
        edits2=fat.objects.get(empid=empid)
        edits2.name=request.POST.get("name")
        edits2.dept=request.POST.get("dept")
        edits2.circle=request.POST.get("circle")
        edits2.location=request.POST.get("location")
        edits2.grade=request.POST.get("grade")
        edits2.date=request.POST.get("date")
        edits2.certno=request.POST.get("certno")
        edits2.status="raw"
        edits2.save()
        return HttpResponse("Data Saved")
    return redirect('/')"""



def printfat(request):
    context = {}
    empid=request.GET.get("empid")
    printdone=fat.objects.get(empid=empid)
    printdone=fat.objects.filter(empid=empid)
    for i in printdone:
        link=i.qrlink
    qr_text = link
    qr_image = qrcode.make(qr_text, box_size=10)
    qr_image_pil = qr_image.get_image()
    stream = BytesIO()
    qr_image_pil.save(stream, format='PNG')
    qr_image_data = stream.getvalue()
    qr_image_base64 = base64.b64encode(qr_image_data).decode('utf-8')
    context['qr_image_base64'] = qr_image_base64
    context['variable'] = qr_text
    return render(request,'print.html',{'printdone':printdone, 'qr_image_base64':qr_image_base64})


"""def printfat(request):
    context = {}
    empid=request.GET.get("empid")
    printdone=fat.objects.get(empid=empid)
    printdone=fat.objects.filter(empid=empid)
    for i in printdone:
        link=i.qrlink
    qr_text = link
    qr_image = qrcode.make(qr_text, box_size=10)
    qr_image_pil = qr_image.get_image()
    stream = BytesIO()
    qr_image_pil.save(stream, format='PNG')
    qr_image_data = stream.getvalue()
    qr_image_base64 = base64.b64encode(qr_image_data).decode('utf-8')
    context['qr_image_base64'] = qr_image_base64
    context['variable'] = qr_text
    userdetail=User.objects.filter(username=email)
    return render(request,'print.html',{'printdone':printdone,'userdetail':userdetail, 'qr_image_base64':qr_image_base64})"""



def donationdetail(request):
    if request.method=="POST":
        context = {}
        amountqr=request.POST.get("amount")
        emailid=request.GET.get("emailid")
        don=donation()
        don.name=request.POST.get("name")
        don.email=request.POST.get("email")
        don.mobile=request.POST.get("mobile")
        don.amount=request.POST.get("amount")
        qr_text = "upi://pay?pa=dhirajpatel08@okaxis&pn=DHIRAJ%20PATEL&am="+amountqr+".00&cu=INR&aid=uGICAgID1xJq5DA"
        qr_image = qrcode.make(qr_text, box_size=15)
        qr_image_pil = qr_image.get_image()
        stream = BytesIO()
        qr_image_pil.save(stream, format='PNG')
        qr_image_data = stream.getvalue()
        qr_image_base64 = base64.b64encode(qr_image_data).decode('utf-8')
        context['qr_image_base64'] = qr_image_base64
        context['variable'] = qr_text
        userdetail=User.objects.filter(username=emailid)
        don.save()
        return render(request,'donationqr.html',{'qr_image_base64':qr_image_base64,'userdetail':userdetail})
    else:
        emailid=request.GET.get("emailid")
        userdetail=User.objects.filter(username=emailid)
        return render(request,'donate.html',{'userdetail':userdetail})


def logintask(req):
    email=req.POST.get("email")
    password=req.POST.get("password")
    user = authenticate(req, username=email, password=password)
    if user is not None:
        userdetail=User.objects.filter(username=email)
        return render(req,'menu.html',{'userdetail':userdetail})
    else:
        messages.error(req,'Invalid Username Or Password')
    return redirect('/')


def logout_view(req):
    auth.logout(req)
    req.session['is_logged']=True
    messages.success(req,'Successfully Logged Out')
    return redirect('/')
