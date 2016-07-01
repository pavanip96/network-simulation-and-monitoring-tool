from __future__ import division
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,render_to_response
from django.db import connection
from django.template import RequestContext
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate,logout
from django.contrib.auth.views import login as auth_login,logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from nettest.models import FileModel,host,testsim2
from nettest.forms import FileForm ,SearchForm ,CaptureForm ,SimulateForm,LoginForm,idForm,RegistrationForm
from nettest.models import EventModel,FileModel,CaptureModel ,SimulateModel,monitable,host
#percentageofpacketup,percentageofpacketdown
from nettest.forms import EventForm
from django.views.generic import CreateView ,View
from django.views.generic import FormView , DetailView
from django.shortcuts import redirect
import csv
import subprocess
import sys
from django.template import RequestContext
import csv
import pymysql
import string
pymysql.install_as_MySQLdb

import datetime
from functools import wraps
import os
def manage(request):
    if request.user.is_authenticated:
        allhosts=host.objects.all()
        i=0
        for hosts in allhosts:
            i=i+1
        context={'hosts':allhosts,'i':i}
        return render(request,'managesys.html',context) 
    return redirect('nettest:registerini')
def deleterow(request):
    
    id=request.POST.get('submit')
    cursor = connection.cursor()
   
    cursor.execute("""delete FROM hosts where id=%s""",(id))
    connection.commit()
    connection.close()
    cursor.close()
    print("deleted")
    return redirect('nettest:manage')
def updaterow(request):

    id=request.POST.get('update')
    pcname = request.POST.get('pcname')
    pcip = request.POST.get('pcip')
    cursor = connection.cursor()
   
    cursor.execute("""update hosts set hostname=%s,hostip=%s where id=%s""",(pcname,pcip,id))
    connection.commit()
    connection.close()
    cursor.close()
       
    return redirect('nettest:manage')
def deleteall(request):
    cursor = connection.cursor()
    cursor.execute("""truncate table hosts""")
    connection.commit()
    connection.close()
    return redirect('nettest:manage')
def counter(func):
    @wraps(func)
    def tmp(*args, **kwargs):
        tmp.count += 1
        return func(*args, **kwargs)
    tmp.count = 0
    return tmp

# Create your views here.
#from django.core.context_processors import csrf

import subprocess
import datetime
sid=1

#login 
def login(request):
    username = password = ''
    
    if request.POST:
        print("login post")
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            print("authenticate")
            if user.is_active:
                
       #redirects to admin interface
                if(username=="admin"):
                 print("user admin")
                 auth_login(request,user)
                 return render(request,'admin.html',{'username':username})
                else :
	#redirects to user interface
                 auth_login(request,user)             
                 return render(request,'home.html',{'username':username})

        else:
                return render(request,'fail.html')
#logout an authenticated user
def logout(request):

    auth_logout(request)
    print("logout")
    return redirect('nettest:registerini')
    
#initiate registration form,redirect to login.html
def registerini(request):

    return render(request,'login.html')
#registers a user
def register(request):
    print("register view")
    if request.POST:
        print("post method")
        form = RegistrationForm(request.POST)
        
        print("form")
        if form.is_valid():
            print("valid form")
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email'])
            return redirect('nettest:registerini')  
    else:
        print("entered else")
        form = RegistrationForm()
    variables = RequestContext(request, {'form': form})
    print("came here")
    
 
    return render(request,'login.html',{'form':form})


def userlist(request):
    if request.user.is_authenticated:



        cursor = connection.cursor()

        
                
        try:
           print("entered try")
           cursor.execute("""SELECT username,date_joined FROM auth_user """)

           
           connection.commit()
        except:
           connection.rollback()

   
        data = cursor.fetchall ()
        connection.close()
        cursor.close()
        print("fetched cursor data")
        for row in data :
          print(row)
        return render(request,'nettest/listusers.html',{'data':data})
    else:
        return redirect('nettest:registerini')

def graphs(request):
    if request.user.is_authenticated:
       print("authenticated")
    

       if request.POST:
        print("post method")

        monid= request.POST.get('monid')
     	print(monid) 
        pcid = request.POST.get('pcid')
	print("pcid")
	print("1")
	print(pcid)	
	print("2")
    
        print("the values are")

        path2script = '/home/ttt/Documents/monitor/changesys/manage/Chmod/projectp/first_project/graphp.R'
	args=[monid,pcid]
	print(args)
#	args2=[pcid]
#	print(args2)
	command='Rscript'
        cmd = [command, path2script]+args

        # check_output will run the command and store to result
        x = subprocess.check_output(cmd, universal_newlines=True)

        print("executed R")
	print(x)
	return render(request,'graphs.html')
       else:
           return render(request,'upload.html')
           
    else:
          return redirect('nettest:registerini')

class FileDetailView(DetailView):
    model = FileModel
    template_name = 'success.html'
    context_object_name = 'file'

class FileEventView(FormView):
    template_name = 'nettest/events.html'
    form_class = EventForm

    


    def form_valid(self, form):
        
        event_up = EventModel()
        event_up.save()
      
        self.id = event_up.id

        return HttpResponseRedirect(self.get_success_url())
        
    
               

    def get_success_url(self):
        return reverse('nettest:eventexe', kwargs={'pk': self.id})
class EventDetailView(DetailView):
    model = FileModel
    template_name = 'nettest/eventexe.html'
   # context_object_name = 'eve'



def admin(request):
    if request.user.is_authenticated:
    
     return render(request,'admin.html')
    return redirect('nettest:registerini')


def searchini(request):
   if request.user.is_authenticated:

    
       return render(request,'search.html')
   else:
       return redirect('nettest:registerini')

def index(request):
    if request.user.is_authenticated:
     return render(request,'homepage.html')
    return redirect('nettest:registerini')

def captureini(request):
   if request.user.is_authenticated:

    
       return render(request,'capture.html')

   else:
      return redirect('nettest:registerini')
class SimulateView(FormView):

    template_name = 'nettest/simulate.html'
    form_class = SimulateForm

    print("hello")
        

    
    def form_valid(self, form):
        
       

        data = SimulateModel(Packets_loss=self.get_form_kwargs().get('data')['Packets_loss'],Jitter=self.get_form_kwargs().get('data')['Jitter'],Latency=self.get_form_kwargs().get('data')['Latency'])
       
        data.save()
             
        return HttpResponseRedirect(self.get_success_url())
       

  
    
               

    def get_success_url(self):
        return reverse('nettest:confirmsim')

    


#Shows a list of clients to select through checkbox
def selecttomonitor(request):
    if request.user.is_authenticated:
        allhosts=host.objects.all()
        i=0
        for hosts in allhosts:
            i=i+1
        context={'hosts':allhosts,'i':i}
        return render(request,'selecttomonitor.html',context) 
    return redirect('nettest:registerini')


#TO add a extra PC to database
def addclienttoselecttomonitor(request):   
    if request.user.is_authenticated:
    #c={}
    #c.update((csrf(request)))
        pcname = request.POST.get('pcname')
        pcip = request.POST.get('pcip')
        addpc=host(hostip=pcip,hostname=pcname)
        addpc.save()
        return HttpResponseRedirect('/nettest/selecttomonitor/')
    return redirect('nettest:registerini')

#After the user has submitted Monitor It starts showing the Clients which you have selected
def showmonitorform(request):
    to_sim=[]
    to_sim=request.POST.getlist("hostid")
    request.session['my_key'] = []
    request.session['my_key'] = to_sim
    #to_sim=map(int,request.POST.getlist("hostid"))
    alist=[]
    src_ip=[]
    for stored_id in to_sim:        
        alist.append(host.objects.get(id=stored_id))
        src_ip.append(host.objects.get(id=stored_id).hostip)
        print (src_ip)
    context={'hosts':alist}
    request.session['allclientips']=[]
    request.session['allclientips']=src_ip
    print (alist)
    return render(request,'showmonitorform.html',context)


#Shows a list of clients to select through checkbox

def selecttosimulate(request):
    if request.user.is_authenticated:
        allhosts=host.objects.all()
        i=0
        for hosts in allhosts:
            i=i+1
        context={'hosts':allhosts,'i':i}
        return render(request,'selecttosimulate.html',context) 
    return redirect('nettest:registerini')

#TO add a extra PC to database
def addclienttoselecttosimulate(request):   
    if request.user.is_authenticated:
    #c={}
    #c.update((csrf(request)))
        pcname = request.POST.get('pcname')
        pcip = request.POST.get('pcip')
        addpc=host(hostip=pcip,hostname=pcname)
        addpc.save()
        return HttpResponseRedirect('/nettest/selecttosimulate/')
    return redirect('nettest:registerini')

def showsimulationform(request):
    if request.user.is_authenticated:
        to_sim=[]
        src_ip=[]
        to_sim=request.POST.getlist("hostid")
        request.session['my_key'] = []
        request.session['my_key'] = to_sim
    #to_sim=map(int,request.POST.getlist("hostid"))
        alist=[]
        for stored_id in to_sim:
            alist.append(host.objects.get(id=stored_id))
            src_ip.append(host.objects.get(id=stored_id).hostip)
            print (src_ip)
        context={'hosts':alist}
        request.session['allclientips']=[]
        request.session['allclientips']=src_ip
        return render(request,'showsimulationform.html',context)
    return redirect('nettest:registerini')


def count(iterable):
    
    return sum(1 for _ in iterable)

def store(request):
  if request.user.is_authenticated:
    if request.POST:
        numberlist = []
        numberlist = request.session['my_key']
    

        print ("Printing ids of selected pcs")
        print (numberlist)
        checked_list=[]
        checked_list=request.POST.getlist("checkifud")
        print ("Printing if upload or download selected")
        print (checked_list)
        #request.session['my_check'] = checked_list
        uploadobj=[]
        downloadobj=[]
        flagu=0
        flagd=0
	#request.session['upload']={}
        #request.session['download']={}
        for j in checked_list:
            print ("j is ")
            print (j)
            if int(j)==1:#Upload Form
                print ("upload done")
                flagu=1
                src_ip=[]
                pc_names=[]
                bnd=[]
                delay=[]
                Jitter=[]
                pkt_loss=[]
                for i in  numberlist:
                    print(i)
                    this_host=host.objects.get(id=i)    
                    source=this_host.hostip 
                    name=this_host.hostname
                    Delay = request.POST.get('delay*'+str(i))
                    jitter = request.POST.get('jitter*'+str(i))
                    packetloss=request.POST.get('loss*'+str(i))
                    band = request.POST.get('bw*'+str(i))
                    new_simobj=testsim2(pc_name=name,source=source,delay=Delay,jitter=jitter,packetloss=packetloss,band=band,character='U',dest="Narayan") 
                    uploadobj.append(new_simobj)  
                    new_simobj.save()
                    pc_names.append(name)
                    src_ip.append(source)
                    bnd.append(band)
                    delay.append(Delay)
                    Jitter.append(jitter)
                    pkt_loss.append(packetloss)
		#request.session['upload'] = {'key0':src_ip,'key1':pc_names,'key2':delay,'key3':Jitter,'key4':pkt_loss,'key5':bnd}	
                a=len(src_ip)	
                ifaceu="eth0"
                cmd1="sudo tc qdisc del dev "+ifaceu+" root"
                subprocess.call(cmd1,shell=True)
                print (cmd1) 
                cmd1="tc qdisc add dev "+ifaceu+" root handle 1: htb default 11"       
                subprocess.call(cmd1,shell=True) 
                print (cmd1) 
                for i in range(1,a+1):
		    #temp_string="bandwidth"+str(i)
		    #bnd.append(request.POST.get(temp_string,''))
                    number=10+i
                    cmd2="sudo tc class add dev "+ifaceu+" parent 1: classid 1:"+str(number)+" htb rate "+str(bnd[i-1])+"kbit"		
                    print (cmd2)
                    subprocess.call(cmd2,shell=True)
                for i in range(1,a+1):
	            #temp_delay="Delay"+str(i)
	 	    #temp_jitter="Jitter"+str(i)
		    #temp_loss="ploss"+str(i)
                    number=10+i
                    handle=100*i
		    #delay.append(request.POST.get(temp_delay,''))
		    #Jitter.append(request.POST.get(temp_jitter,''))
		    #pkt_loss.append(request.POST.get(temp_loss,''))
                    cmd3="sudo tc qdisc add dev "+ifaceu+" parent 1:"+str(number)+" handle "+str(handle)+": netem delay "+str(delay[i-1])+"ms "+str(Jitter[i-1])+"ms loss "+str(pkt_loss[i-1])+"%"
                    print (cmd3)
                    subprocess.call(cmd3,shell=True)
                for i in range(1,a+1):
                    number=10+i
		    #temp_string="source"+str(i)
		    #src_ip.append(request.POST.get(temp_string,''))
                    cmd4="sudo tc filter add dev "+ifaceu+" protocol ip prio 1 u32 match ip src "+str(src_ip[i-1])+" flowid 1:"+str(number)
                    print (cmd4)
                    subprocess.call(cmd4,shell=True) 
            elif int(j)==2:#Download form
                flagd=1
                src_ip=[]
                pc_names=[]
                bnd=[]
                delay=[]
                Jitter=[]
                pkt_loss=[]
                print ("Download done")
                for i in numberlist:
                    print(i)
                    this_host=host.objects.get(id=i)    
                    source=this_host.hostip 
                    name=this_host.hostname
                    Delay = request.POST.get('delayd*'+str(i))
                    jitter = request.POST.get('jitterd*'+str(i))
                    packetloss=request.POST.get('lossd*'+str(i))
                    band = request.POST.get('bwd*'+str(i))
                    new_simobj=testsim2(pc_name=name,source=source,delay=Delay,jitter=jitter,packetloss=packetloss,band=band,character='D',dest="Uddhav")
                    downloadobj.append(new_simobj) 
                    new_simobj.save()
                    src_ip.append(source)
                    pc_names.append(name)
                    bnd.append(band)
                    delay.append(Delay)
                    Jitter.append(jitter)
                    pkt_loss.append(packetloss)
		#request.session['download'] = {'key0':src_ip,'key1':pc_names,'key2':delay,'key3':Jitter,'key4':pkt_loss,'key5':bnd}	
                a=len(src_ip)				
                ifaceu="eth1"
                cmd1="sudo tc qdisc del dev "+ifaceu+" root"
                subprocess.call(cmd1,shell=True)
                print (cmd1) 
                cmd1="sudo tc qdisc add dev "+ifaceu+" root handle 1: htb default 11"       
                subprocess.call(cmd1,shell=True) 
                print (cmd1) 
                for i in range(1,a+1):
		    #temp_string="bandwidth"+str(i)
		    #bnd.append(request.POST.get(temp_string,''))
                    number=10+i
                    cmd2="sudo tc class add dev "+ifaceu+" parent 1: classid 1:"+str(number)+" htb rate "+str(bnd[i-1])+"kbit"		
                    print (cmd2)
                    subprocess.call(cmd2,shell=True)
                for i in range(1,a+1):
	            #temp_delay="Delay"+str(i)
	 	    #temp_jitter="Jitter"+str(i)
		    #temp_loss="ploss"+str(i)
                    number=10+i
                    handle=100*i
		    #delay.append(request.POST.get(temp_delay,''))
		    #Jitter.append(request.POST.get(temp_jitter,''))
		    #pkt_loss.append(request.POST.get(temp_loss,''))
                    cmd3="sudo tc qdisc add dev "+ifaceu+" parent 1:"+str(number)+" handle "+str(handle)+": netem delay "+str(delay[i-1])+"ms "+str(Jitter[i-1])+"ms loss "+str(pkt_loss[i-1])+"%"
                    print (cmd3)
                    subprocess.call(cmd3,shell=True)
                for i in range(1,a+1):
                    number=10+i
		    #temp_string="source"+str(i)
		    #src_ip.append(request.POST.get(temp_string,''))
                    cmd4="sudo tc filter add dev "+ifaceu+" protocol ip prio 1 u32 match ip dst "+str(src_ip[i-1])+" flowid 1:"+str(number)
                    print (cmd4)
                    subprocess.call(cmd4,shell=True) 		
        if len(checked_list)!=0: 	#To be changed by javascript	
            #print len(checked_list)
            print ("HIHIHIHIHIHIHIHIHIH")			      
            text={"upload":uploadobj,"download":downloadobj,"i":flagu,"j":flagd}                			
            return render(request,'simulatemonitorform.html',text)
        else:
            print ("Not selected Anything size of checklist is zero")
            alist=[]
            for stored_id in numberlist:
                alist.append(host.objects.get(id=stored_id)) 
            context={'hosts':alist}
            return render(request,'showsimulationform.html',context)

    return render(request,'showsimulationform.html')

  return redirect('nettest:registerini')

def execute(request):
    if request.user.is_authenticated:


     y="hello"
    
     print("the values are")
     args=[Time]

     command = 'Rscript'
     path2script = 'C:/Users/P PRABHAKAR/Desktop/csvg/display/plotgupd.R'

     cmd = [command, path2script]+args

        # check_output will run the command and store to result
     x = subprocess.check_output(cmd, universal_newlines=True)

     #myscript = subprocess.Popen(['Rscript','nettest/plotgup.R'],shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
     print("executed R")
   
                                 
     print(x)
     ifile  = open('C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/writefile.csv', "r", encoding="utf-8")



     cursor = connection.cursor()

     
     print("started sql")
     try:
         sql = """LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/writefile.csv' INTO TABLE nettest_test10 FIELDS TERMINATED BY ','  IGNORE 1 LINES   (dates, ips, ipd,sumup,sumdown,meanup, meandown,bandup, banddown) """
     
         cursor.execute(sql)
         print("Executed")
     except:
          connection.rollback()
        
     connection.commit()
   

     data = cursor.fetchall ()
     for row in data :
      
      print(row)

     sql="""LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/results.csv' INTO TABLE nettest_results FIELDS TERMINATED BY ','  IGNORE 1 LINES   (dates, ips, ipd,sumup,sumdown,meanup, meandown,bandup, banddown) """
     cursor.execute(sql)
     connection.commit()
     sql="""SELECT * FROM nettest_results"""
     print("selected")
     cursor.execute(sql)
     connection.commit()
     
     data2=cursor.fetchall()

     sql="""delete FROM nettest_results where id1>=1"""
     
     cursor.execute(sql)
     print("deleted")
     connection.commit()
     
     
     for row in data2:
        print(row)
     
     connection.close()
     
     cursor.close()
    
     return render(request,'execute.html', {"y":y,"data2":data2})
    else:
        return redirect('nettest:registerini')

def searchevent(request):
 if request.user.is_authenticated:

 
    startdate= enddate = ''
    
    if request.POST:
        startdate = request.POST.get('startdate')
        enddate = request.POST.get('enddate')

        y="hii"
        print("hellohi")
        
     
        cursor = connection.cursor()
        print("connectionc")

        
                
        try:
           print("entered try")
           cursor.execute("""SELECT * FROM nettest_test10 WHERE dates between %s and %s  """,(startdate,enddate))

           
           connection.commit()
        except:
           connection.rollback()

   
        data = cursor.fetchall ()
        print("fetched cursor data")
        for row in data :
          print(row)
          print("fetched data")
     

  
        connection.close()
        cursor.close()
        print("render")
        
        

        return render(request,'eventexe.html',{'y':y,'data':data,'startdate':startdate,'enddate':enddate})

        
    return render(request,'search.html')
 return redirect('nettest:registerini')





@counter
def executetshark(request):
    dur=request.POST.get('dur','')
    ip=request.POST.get('server','')#server ip
    Time=request.POST.get('dur')
    request.session['Time']=Time
    
    print ("Got The Server ip")
    cmd1="sudo tshark -i eth1 -a duration:"+str(dur)+" host "+str(ip)+" -w CapFileTest.pcap"
    subprocess.call(cmd1,shell=True)
    print ("Pcap file generated")
    cmd1="sudo tshark -r CapFileTest.pcap -T fields -e ip.src -e ip.dst -e frame.len -E separator=, -Eheader=n >CapFileTestSrc.csv"#-e ip.dst
    subprocess.call(cmd1,shell=True)  
    print ("Main CSV Generated")
    name_file="CapFileTestSrc"  
    command3="sed -i '/TCP Dup/d' "+str(name_file)+".csv"
    command4="sed -i '/TCP Retransmission/d' "+str(name_file)+".csv"
    subprocess.call(command3,shell=True)
    print ("Removed The DUPLICATE  Files")
    subprocess.call(command4,shell=True)    
    print ("Removed The Retransmission Files")
    #result_file=open("CapFileTestSrc.csv",'r')
    #clientup=open("clientupload.csv",'w')
    #clientdown=open("clientdownload.csv",'w')
    serverip=ip
    client_list=[]
    client_list=request.session['allclientips']
    print ("Got the client Ips thrugh session and printing client Ips")
    for ip in client_list:
        print (ip)

    now = datetime.datetime.now()
    datestamp=now.strftime("%Y%m%d-%H:%M:%S")
    id2=""
    for ip in client_list:
        id2=id2+ip+'/'
    
    monid=str(datestamp)+"-M"
    print(monid)
    request.session['monid']=monid

    print ("DONE DONE DONE")	
    print ("Printin through traditinsal way")
    numberlist = []
    numberlist = request.session['my_key']
    client_list2=[]
    for i in numberlist:
        this_host=host.objects.get(id=i)    
        source=this_host.hostip
        client_list2.append(source)
        print (source) 
    #for line in result_file:
    #    a=line.split(',')
    #    if client_list.__contains__(a[0]) and a[1]==serverip:
    #        #print "Hellog2g in clinetup"
    #        clientup.write(line)
    #    elif a[0]==serverip:
    #        clientdown.write(line)

    '''psizeu=dict()
    psized=dict()
    rowu=dict()
    rowd=dict()
    linecnt=0
    for ip in client_list:
        psizeu[str(ip)]=0
        psized[str(ip)]=0
        rowu[str(ip)]=0
  	rowd[str(ip)]=0
    print "Going to for loop"
    subprocess.call("pwd",shell=True)
    resultfile=open('CapFileTestSrc.csv','r+')
    print resultfile.name
    for line in resultfile:
	print line       
	a=line.split(',')
        linecnt=linecnt+1
        if client_list.__contains__(a[0]) and a[1]==serverip:
            psizeu[str(a[0])]=psizeu[str(a[0])]+int(a[2])
	    rowu[str(a[0])]=int(rowu[str(a[0])])+1
	    print "uplo"
	    print a[0],
	    print rowu[a[0]]
	    #clientup.write(line)
        elif a[0]==serverip and client_list__contains__(a[1]):
            psized[str(a[1])]=psized[str(a[1])+int(a[2])
	    rowd[str(a[1])]=int(rowd[str(a[1])])+1
	    print "down"
	    print a[1],
	    print rowd[a[0]] 
	    #clientdown.write(line)
    tdur=int(dur)-1
    client_list
    for ip in client_list:
		print ip	
		print dict[str(ip)]
		print (dict[str(ip)]*1.00)
		mup=((psizeu[str(ip)])/(rowu_dict[str(ip)]*1.00))
		mdwn= (psized[str(ip)]/(rowd_dict[str(ip)]*1.00))
		apups=rowu[str(ip)]/(tdur*1.00)
		apdps=rowd[str(ip)]/(tdur*1.00)
		print mup
		print mdwn
		print apups
		print apdps
                print "Bandwidth Up and Bandwidth Down "
                print apups*mup
        	print mdwn*apdps
	        tobj=mdetails(mip=ip,mtime=dur,mtotal_pkt=linecnt,sumup=psizeu_dict[str(ip)],sumdown=psized_dict[str(ip)],meanup=mup,meandown=mdwn,avg_u_s=(apups),avg_d_s=(apdps),bandup=(apups*mup),banddown=(mdwn*apdps))
	        tobj.save()'''
    '''psizeu_dict={}
    psized_dict={}
    rowu_dict={}
    rowd_dict={}
    linecnt=0
    for ip in client_list:
        psizeu_dict[str(ip)]=0
        psized_dict[str(ip)]=0
        rowd_dict[str(ip)]=0
        rowu_dict[str(ip)]=0
    result_file=open("CapFileTestSrc.csv",'r')
    for line in result_file:
	print "Hello print in line"
        a=line.split(',')
        linecnt+=1
        if client_list.__contains__(a[0]) and a[1]==serverip:
            psizeu_dict[str(a[0])]+=int(a[2])
            rowu_dict[str(a[0])]+=1
            #clientup.write(line)
        elif a[0]==serverip and client_list.__contains__(a[1]):
            psized_dict[str(a[1])]+=int(a[2])
            rowd_dict[str(a[1])]+=1
            #clientdown.write(line)
    for ip in client_list:
        print ip
	print psizeu_dict[str(ip)]
	print rowu_dict[str(ip)]
	print rowd_dict[str(ip)]
	print psized_dict[str(ip)]
	mup=(psizeu_dict[str(ip)]/(rowu_dict[str(ip)]*1.00))
        mdwn= (psized_dict[str(ip)]/(rowd_dict[str(ip)]*1.00))
        apups=rowu_dict[str(ip)]/(dur*1.00)
        apdps=rowd_dict[str(ip)]/(dur*1.00)
        print mup
        print mdwn
        print apups
        print apdps
        print "Bandwidth Up and Bandwidth Down"
        print mup*apups
        print mdwn*apdps'''

    #TO add 
    result_file=open("CapFileTestSrc.csv",'r')

    for line in result_file:
#	print("forloop")
        a=line.split(',')
#	print(a)
#	print(serverip)
#	print(client_list)	
#	print(client_list.__contains__((a[0])))
        if client_list.__contains__((a[0])) and a[1]==serverip:
#	    print("if ")
            file=open("/home/ttt/Documents/monitor/changesys/manage/Chmod/projectp/first_project/download/up"+str(a[0])+".csv",'a')
            file.write(line)
            #t_s="up"+str(a[0])
	    #print t_s
        elif a[0]==serverip and client_list.__contains__((a[1])):
            print("elif")
            file=open("/home/ttt/Documents/monitor/changesys/manage/Chmod/projectp/first_project/download/down"+str(a[1])+".csv",'a')
            file.write(line)
	    #t_s="down"+str(a[1])
	    #print t_s

    print ("clientup and client down csv files generated")

    cmd1 = "sudo tc qdisc del dev eth0 root"
    subprocess.call(cmd1,shell=True)
    print (cmd1)
    cmd1="sudo tc qdisc del dev eth1 root"
    subprocess.call(cmd1,shell=True)
    print (cmd1)
    cmd1="sudo tc qdisc del dev eth2 root"
    subprocess.call(cmd1,shell=True)
    print (cmd1)
    print ("SUNNY L")
    return redirect('nettest:capture')


def captureini(request):
   if request.user.is_authenticated:

    
       return render(request,'capture.html')
   else:
      return redirect('nettest:registerini')

def capture(request):
   if request.user.is_authenticated:

       
    Time = ''
    
    
    if request.POST :
        
     #   Time = request.POST.get('Time')
        
        cursor = connection.cursor()
        Time=request.session['Time']

        monid=request.session['monid']
        print(monid)

        print(Time)

        command = 'Rscript' 
        path2script = "/home/ttt/Documents/monitor/changesys/manage/Chmod/projectp/first_project/testing.R"
        
        args = [Time] 
        cmd = [command, path2script] + args

        x = subprocess.check_output(cmd, universal_newlines=True)

	with open("/home/ttt/Documents/monitor/changesys/manage/Chmod/projectp/first_project/storedb.csv") as f:
            dataReader = csv.reader(f, delimiter=',',quotechar='"')
            for row in dataReader:
                moni = monitable()
                moni.monid=monid
                moni.dates = row[0]
                moni.ips = row[1]
                moni.ipd= row[2]

                cursor.execute("""select hostname from hosts where hostip = %s""",(moni.ips))
                connection.commit()
                
                pcid=cursor.fetchone()
                pcid=str(pcid)
                pcid=pcid.replace(")","")
                pcid=pcid.replace(",","")
                pcid=pcid.replace("(","")
                pcid=pcid.replace("'","")
                moni.pcid=pcid
                

                moni.totalpacketsup =row[3]
                moni.totalpacketsdown= row[4]
                moni.totalpackets = row[5]
                moni.sumup = row[6]
                moni.meanup = row[7]
                moni.bandup=row[8]
                moni.sumdown= row[9]
                moni.meandown = row[10]
                moni.banddown=row[11]
                
                
     
                moni.save()
        with open('/home/ttt/Documents/monitor/changesys/manage/Chmod/projectp/first_project/packperc.csv') as z:
            dataReader2 = csv.reader(z, delimiter=',',quotechar='"')
            for row in dataReader2:
                pp=percentageofpacketup()
                pp.monid1=monid
                pp.ips1=row[0]
                print(pp.ips1)
                cursor.execute("""select hostname from hosts where hostip = %s""",(pp.ips1))
                connection.commit()
                
                pcid=cursor.fetchone()
                pcid=str(pcid)
                pcid=pcid.replace(")","")
                pcid=pcid.replace(",","")
                pcid=pcid.replace("(","")
                pcid=pcid.replace("'","")
                pp.pcid=pcid
                pp.p1_p250=row[1]
                
                pp.p251_p500=row[2]
                pp.p501_p750=row[3]
                pp.p751_p1000=row[4]
		pp.p1001_p1250=row[5]
	        pp.p1251_p1500=row[6]
                pp.p1501_p1750=row[7]
                pp.p1751=row[8]
                pp.totup=row[17]
                pp.save()

                pp2=percentageofpacketdown()
                pp2.monid1=monid
                pp2.ips1=row[0]
                cursor.execute("""select hostname from hosts where hostip = %s""",(pp2.ips1))
                connection.commit()
                
                pcid=cursor.fetchone()
                pcid=str(pcid)
                pcid=pcid.replace(")","")
                pcid=pcid.replace(",","")
                pcid=pcid.replace("(","")
                pcid=pcid.replace("'","")
                pp2.pcid=pcid
                pp2.p1_p250=row[9]
                
                pp2.p251_p500=row[10]
                pp2.p501_p750=row[11]
                pp2.p751_1000=row[12]
                pp2.p1001_p1250=row[13]

                pp2.p1251_p1500=row[14]
                pp2.p1501_p1750=row[15]
                pp2.p1751=row[16]
                pp2.totdown=row[18]
                pp2.save()
                

                
                
                
        sql="""select * from nettest_monitable"""
        cursor.execute(sql)
        connection.commit()
     #   f.close()

        data3=cursor.fetchall()

        os.remove('/home/ttt/Documents/monitor/changesys/manage/Chmod/projectp/first_project/storedb.csv')
           
     #   cmdlone="rm -rf /home/ttt/Documents/monitor/changesys/manage/Chmod/projectp/first_project/download/*"
        sql="""truncate nettest_monitable"""
        cursor.execute(sql)
        connection.commit()
      #  subprocess.call(cmdlone,shell=True)
        return render(request,'confirm.html',{'x':x,'data3':data3})

        
    return render(request,'capture.html')
        
    '''         
def doexecutetc(request,total_client):

 if request.user.is_authenticated:
  #  c={}
   # c.update((csrf(request)))
    #print total_client
    command1="sudo tc qdisc del dev eth2 root"
    subprocess.call(command1,shell=True) 
    src_ip=[]
    bnd=[]
    delay=[]
    Jitter=[]
    pkt_loss=[]
    a=int(total_client)
    cmd1="tc qdisc add dev eth2 root handle 1: htb default 11"       
    subprocess.call(cmd1,shell=True)
    for i in range(1,a+1):
        temp_string="bandwidth"+str(i)
        bnd.append(request.POST.get(temp_string,''))
        number=10+i
        cmd2="tc class add dev eth2 parent 1 classid 1:"+str(number)+" htb rate "+str(bnd[i-1])+"kbit"		
	#print cmd2
        subprocess.call(cmd2,shell=True)
    for i in range(1,a+1):
        temp_delay="Delay"+str(i)
        temp_jitter="Jitter"+str(i)
        temp_loss="ploss"+str(i)
        number=10+i
        handle=100*i
        delay.append(request.POST.get(temp_delay,''))
        Jitter.append(request.POST.get(temp_jitter,''))
        pkt_loss.append(request.POST.get(temp_loss,''))
        cmd3="tc qdisc add dev eth2 parent 1:"+str(number)+" handle "+str(handle)+": netem delay "+str(delay[i-1])+"ms "+str(Jitter[i-1])+"ms loss "+str(pkt_loss[i-1])+"%"
        #print cmd3
        subprocess.call(cmd3,shell=True)
    for i in range(1,a+1):
        number=10+i
        temp_string="source"+str(i)
        src_ip.append(request.POST.get(temp_string,''))
        cmd4="tc filter add dev eth2 protocol ip prio 1 u32 match ip src "+str(src_ip[i-1])+" flowid 1:"+str(number)
        #print cmd4
        subprocess.call(cmd4,shell=True)
    Delay=request.POST.get('Delay','')
    Jitter=request.POST.get('Jitter','')
    ploss=request.POST.get('ploss','')
    bandwidth=request.POST.get('bandwidth','')
    #print Delay
    #print Jitter
    #print ploss
    #print bandwidth    
    command1="sudo tc qdisc del dev eth2 root"
    subprocess.call(command1,shell=True)
    #print "Deleted previous configs"
    str1="delay "+Delay+"ms "+Jitter+"ms loss "+ploss+"%"
    command2="sudo tc qdisc add dev eth2 root handle 1: netem "+str(str1)
    subprocess.call(command2,shell=True)
    #print("Configured bandwidth on the upload side")
    command3="sudo tc qdisc add dev eth2 parent 1: handle 2: tbf rate "+str(bandwidth)+"Kbit burst 1600 limit 3000"
    subprocess.call(command3,shell=True)
    #print("Configured Delay jitter loss")
    #print ("Cnfigured the Entire Simulation part")
    verify="tc qdisc show dev eth2"
    subprocess.call(verify,shell=True
    return HttpResponse("TC Command Executed Go Monitor to start tshark ")
 return redirect('nettest:registerini')
'''

'''
def doexecutetshark(request,total_client):
 if request.user.is_authenticated:
   # c={}
    #c.update((csrf(request)))
    #print total_client
    ip_source=[]
    dur=request.POST.get('dur','')
    ip=request.POST.get('server','')#server ip
    command1="sudo tshark -i eth2 -a duration:"+str(dur)+" host "+str(ip)+" -w CapFileTest.pcap"
    subprocess.call(command1,shell=True)
    #print "Tshark pcap file generated Starting Command Two"
    command2="sudo tshark -r CapFileTest.pcap -T fields -e ip.src -e ip.dst -e frame.len -E separator=, -Eheader=y >CapFileTestSrc.csv"#-e ip.dst
    subprocess.call(command2,shell=True)
    #print "Source CSV File generated"
    for i in range(1,int(total_client)+1):
        temp_string="source"+i
        name_file='ClientUp'+i
        name_file_down='ClientDown'+i
        ip_source.append(request.POST.get(temp_string,''))
        com_t='tshark -Y "ip.src == '+str(ip_source[i-1])+' && ip.dst == '+str(ip)+'" -r CapFileTest.pcap >'+str(name_file)+'-.csv'
        subprocess.call(com_t,shell=True)
        command3="sed -i '/TCP Dup/d' "+str(name_file)+".csv"
        command4="sed -i '/TCP Retransmission/d' "+str(name_file)+".csv"
        #print "Duplicate Ip deleted for Upload file"
        subprocess.call(command3,shell=True)
        #print "Retransmission Ip deleted for Upload File"
        subprocess.call(command4,shell=True)
        comm_t='tshark -Y "ip.dst == '+str(ip_source[i-1])+' && ip.src == '+str(ip)+'" -r CapFileTest.pcap >'+str(name_file_down)+'-.csv'      
        subprocess.call(comm_t,shell=True)
        command3="sed -i '/TCP Dup/d' "+str(name_file_down)+".csv"
        command4="sed -i '/TCP Retransmission/d' "+str(name_file_down)+".csv"
	#print "Duplicate Ip deleted for Upload file"
        subprocess.call(command3,shell=True)
	#print "Retransmission Ip deleted for Upload File"
        subprocess.call(command4,shell=True)
    cip=request.POST.get('cip','')
    client_ip=get_client_ip(request)
    #print dur
    #print ip
    #print cip
    #print client_ip
    now =datetime.datetime.now()
    filename= now.strftime("%Y-%m-%d %H:%M:%S")
    pcapfile="CapFileTest"+str(filename)+".pcap"
    command1="sudo tshark -i eth2 -a duration:"+str(dur)+" host "+str(ip)+" -w CapFileTest.pcap"
    subprocess.call(command1,shell=True)
    #print "Tshark pcap file generated Starting Command Two"
    command2="sudo tshark -r CapFileTest.pcap -T fields -e ip.src -e frame.len -E separator=, -Eheader=y >CapFileTestSrc.csv"#-e ip.dst
    subprocess.call(command2,shell=True)
    #print "Source CSV File generated"
    command3="sed -i '/TCP Dup/d' CapFileTestSrc.csv"
    command4="sed -i '/TCP Retransmission/d' CapFileTestSrc.csv"
    subprocess.call(command3,shell=True)
    #print "Duplicate IP deleted"
    subprocess.call(command4,shell=True)
    #print "Retransission Ip deleted"
    #commandgrep="grep -i "+"'"+str(client_ip)+","+str(ip)+"' CapFileTestSrc.csv > CApFileTestSrc.csv"    
    commandgrep1="grep -i '"+cip+"' CapFileTestSrc.csv > ClientUp.csv"
    subprocess.call(commandgrep1,shell=True)
    #print "1 Upload File Generated"
    commandgrep2="grep -i '"+ip+"' CapFileTestSrc.csv > ClientDown.csv"
    subprocess.call(commandgrep2,shell=True)
    #print "Download File Generated
    return HttpResponse("Tshark Command executed and csv file is generated")
 return redirect('nettest:registerini')
'''

def get_client_ip(request):
  if request.user.is_authenticated:
      
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
  return redirect('nettest:registerini')
