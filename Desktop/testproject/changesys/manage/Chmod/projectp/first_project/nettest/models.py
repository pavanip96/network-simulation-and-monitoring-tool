from __future__ import unicode_literals
from django.db import models
from django.contrib.admin.widgets import AdminDateWidget
from django.db.models.fields import DateField, DateTimeField
from django.utils import timezone
from datetime import datetime

from django.db import models
from django.contrib.admin.widgets import AdminDateWidget
from django.db.models.fields import DateField, DateTimeField
from django.utils import timezone
from datetime import datetime

class testsim2(models.Model):
    simid=models.CharField(max_length=50,null=True,blank=True)    
    dest=models.CharField(max_length=50,null=True,blank=True)
    source=models.CharField(max_length=50,null=True,blank=True)
    pc_name=models.CharField(max_length = 30,null=True,blank=True)
    delay=models.IntegerField(null=True,blank=True)
    jitter=models.IntegerField(null=True,blank=True)
    packetloss=models.FloatField(null=True,blank=True)
    band=models.FloatField(null=True,blank=True)
    character=models.CharField(max_length=50,null=True,blank=True)

'''
class mdetails(models.Model):
   
    mip=models.CharField(max_length=50,null=True,blank=True)
    mtime=models.IntegerField()
    mtotal_pkt=models.IntegerField()
    sumup=models.IntegerField(null=True,blank=True)
    sumdown=models.IntegerField(null=True,blank=True)
    meanup=models.FloatField(null=True,blank=True)
    meandown=models.FloatField(null=True,blank=True)
    avg_u_s=models.FloatField(null=True,blank=True)
    avg_d_s=models.FloatField(null=True,blank=True)
    bandup=models.CharField(max_length=50,null=True,blank=True)
    banddown=models.CharField(max_length=50,null=True,blank=True)
    class Meta:
        db_table="mdetails"
   '''     

class host(models.Model):
    hostip = models.CharField(max_length = 30)
    hostname = models.CharField(max_length = 30)
    opsystem=models.CharField(max_length=30,null=True,blank=True)
    ram=models.CharField(max_length=30,null=True,blank=True)
    processor=models.CharField(max_length=30,null=True,blank=True)
    class Meta:
        db_table="hosts"

    
class CaptureModel(models.Model):
    Time = models.CharField(max_length=30)
    
    fields = '__all__'
#class test10(models.Model):
    
 #   dates=models.DateField(blank=True,null=True)
 #   ips=models.CharField(max_length=50,null=True,blank=True)
 #   ipd=models.CharField(max_length=50,null=True,blank=True)
 #   sumup=models.IntegerField(null=True,blank=True)
 #   sumdown=models.IntegerField(null=True,blank=True)
 #   meanup=models.FloatField(null=True,blank=True)
 #   meandown=models.FloatField(null=True,blank=True)
 #   bandup=models.CharField(max_length=50,null=True,blank=True)
 #   banddown=models.CharField(max_length=50,null=True,blank=True)
 #   fields = '__all__'

class capture(models.Model):
    id1 = models.AutoField(primary_key=True)
    dates=models.DateField(blank=True,null=True)
    ips=models.CharField(max_length=50,null=True,blank=True)
    ipd=models.CharField(max_length=50,null=True,blank=True)
    sum1=models.IntegerField(null=True,blank=True)
    sum2=models.IntegerField(null=True,blank=True)
    mean1=models.FloatField(null=True,blank=True)
    mean2=models.FloatField(null=True,blank=True)
    bandup=models.CharField(max_length=50,null=True,blank=True)
    banddown=models.CharField(max_length=50,null=True,blank=True)
    fields = '__all__'

class monitable(models.Model):
    id1=models.AutoField(primary_key=True)
    simid=models.CharField(max_length=200,null=True,blank=True)
    monid=models.CharField(max_length=200,null=True,blank=True)
    pcid=models.CharField(max_length=200,null=True,blank=True)
    
    dates=models.DateField(blank=True,null=True)
    ips=models.CharField(max_length=50,null=True,blank=True)
    ipd=models.CharField(max_length=50,null=True,blank=True)
    totalpacketsup=models.IntegerField(null=True,blank=True)
    totalpacketsdown=models.IntegerField(null=True)
    totalpackets=models.IntegerField(null=True)
    sumup=models.IntegerField(null=True,blank=True)
    meanup=models.FloatField(null=True,blank=True)
    bandup=models.CharField(max_length=50,null=True,blank=True)

    sumdown=models.IntegerField(null=True,blank=True)
   
    meandown=models.FloatField(null=True,blank=True)
    banddown=models.CharField(max_length=50,null=True,blank=True)
    fields = '__all__'

class percentageofpacketup(models.Model):
    monid1=models.CharField(max_length=200,null=True,blank=True)
    pcid=models.CharField(max_length=200,null=True,blank=True)
    ips1=models.CharField(max_length=50,null=True,blank=True)
    p1_p250=models.IntegerField(null=True,blank=True)
    p251_p500=models.IntegerField(null=True,blank=True)
    p501_p750=models.IntegerField(null=True,blank=True)
    p751_p1000=models.IntegerField(null=True,blank=True)
    p1001_p1250=models.IntegerField(null=True,blank=True)
    p1251_p1500=models.IntegerField(null=True,blank=True)
    p1501_p1750=models.IntegerField(null=True,blank=True)
    p1751=models.IntegerField(null=True,blank=True)
    totup=models.IntegerField(null=True,blank=True)

class percentageofpacketdown(models.Model):
    monid1=models.CharField(max_length=200,null=True,blank=True)
    pcid=models.CharField(max_length=200,null=True,blank=True)
    ips1=models.CharField(max_length=50,null=True,blank=True)
    p1_p250=models.IntegerField(null=True,blank=True)
    p251_p500=models.IntegerField(null=True,blank=True)
    p501_p750=models.IntegerField(null=True,blank=True)
    p751_p1000=models.IntegerField(null=True,blank=True)
    p1001_p1250=models.IntegerField(null=True,blank=True)
    p1251_p1500=models.IntegerField(null=True,blank=True)
    p1501_p1750=models.IntegerField(null=True,blank=True)
    p1751=models.IntegerField(null=True,blank=True)
    totdown=models.IntegerField(null=True,blank=True)




class SimulateModel(models.Model):
    Packets_loss=models.IntegerField()
    Jitter=models.IntegerField()
    Latency=models.IntegerField()
    fields = '__all__'

class FileModel(models.Model):
    file=models.FileField(upload_to='C:/Users/P PRABHAKAR/Desktop/csvg/')
    file2=models.FileField(upload_to='C:/Users/P PRABHAKAR/Desktop/csvg/')
    fields = '__all__'

class Onemodel(models.Model):
    x=models.IntegerField()
class EventModel(models.Model):
    
    first_name = models.CharField(max_length=30)
    event_description = models.CharField(max_length=200)
    startdate = models.DateField( blank=True,null=True)

    fields='__all__'
    def __str__(self):
          return self.event_description

class SearchModel(models.Model):

    startdate = models.DateField( blank=True,null=True)
    enddate=models.DateField( blank=True,null=True)

    
    fields='__all__'





