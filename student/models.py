from django.db import models
import os
import datetime
# Create your models here.

def filepath(req,filename):
   old_filename = filename
   timeNow = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
   filename= "%s%s" % (timeNow,old_filename)
   return os.path.join('uploads/',filename)

   
class fat(models.Model):
	name=models.CharField(max_length=15)
	empid=models.CharField(max_length=15)
	dept=models.CharField(max_length=15)
	circle=models.CharField(max_length=15)
	location=models.CharField(max_length=40)
	grade=models.CharField(max_length=100)
	date=models.CharField(max_length=15)
	certno=models.CharField(max_length=15)
	image=models.ImageField(upload_to=filepath,null=True,blank=True)
	qr=models.ImageField(upload_to=filepath,null=True,blank=True)
	status=models.CharField(max_length=15,null=True,default="raw")
	qrlink=models.CharField(max_length=15,null=True)

def __str__(self):
	return self.name


class donation(models.Model):
	name=models.CharField(max_length=50)
	email=models.CharField(max_length=50)
	mobile=models.CharField(max_length=15)
	amount=models.CharField(max_length=10)

def __str__(self):
	return self.name
