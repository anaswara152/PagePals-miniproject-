from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.contrib import messages
from librarian.models import*
import datetime

# Create your views here.
def home(request):
      return render(request,'common/home.html')

def studenthome(request):
     return render(request,'student/shome.html',)

def registration(request):
        if  request.method == 'POST':
                name=request.POST['name']
                age=request.POST['age']
                gender=request.POST['gender']
                address=request.POST['address']
                username=request.POST['username']
                password=request.POST['password']
                if len(request.FILES)>0:
                     img=request.FILES['file']
                else:
                  img="no pic"
                m=student.objects.create(name=name,age=age,gender=gender,address=address,username=username,password=password,profilephoto=img)
                m.save()
                messages.info(request,'registration is sucessfull')
        return render(request,"student/register.html")


def login(request):
    if 'id' in request.session and 'role' in request.session:
         if request.session['role']=='librarian':
              return redirect('adminhome')
         else:
              return redirect('studenthome')
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        admin=library.objects.filter(username=username,password=password).first()
        student1=student.objects.filter(username=username,password=password).first()
        if admin:
            request.session['id']=admin.id
            request.session['role']='librarian'
            return redirect('adminhome')
        elif student1:
            request.session['id']=student1.id
            request.session['role']='student'

            return redirect('studenthome')        
        else:
              messages.error(request,'invalid credential')

    return render(request,'common/login.html') 

 
def logout(request):
      if 'id' in request.session:
           request.session.flush()
      return redirect('home')


def viewbooks(request):
     b=book.objects.all()
     return render(request,'student/vbook.html',{'b':b})


def bookingbook(request,id):
      book1=book.objects.filter(id=id)
      studentid=request.session['id']
      date=datetime.datetime.now()
      number=book1[0].numberof_copies 
      if number==0:
            messages.info(request,'can not get the book')    
            return redirect('viewbooks') 
      else:
            ab=booking.objects.create(bookid_id=id,studentid_id=studentid,booking_date=date,return_date="null")   
            ab.save()
            quantity=number-1
            p=book1.update(numberof_copies=quantity)
      return redirect('viewbooks')

def viewbooking(request):        
      std=request.session['id']
      ab=booking.objects.filter(studentid_id=std,status='pending')
      s={'m':ab}
      return render(request,'student/viewbooking.html',s)
def returnbook(request,id):
      date=datetime.datetime.now()
      booking.objects.filter(id=id).update(status="returned",return_date=date)
      return redirect('viewbooking')


def newpassword(request):
      if request.method=="POST":
            old_password=request.POST['old_password']
            new_password=request.POST['new_password']
            confirm_password=request.POST['confirm_password']
            if new_password==confirm_password:
                  data=student.objects.filter(password=old_password)
                  if data.count()>0:
                        n=student.objects.filter(id=data[0].id).update(password=new_password)
                        messages.info(request,'password changed')
            else:
                  messages.info(request,'incorrect password')
                  return redirect('reservedbook')
      return render(request,'student/newpassword.html')   


def viewprofile(request):
      ab=student.objects.get(id=request.session['id'])  
      h={'m':ab}  
      return render(request,'student/viewprofile.html',h) 

def editprofile(request):
    sid = request.session['id']
    s = get_object_or_404(student, id=sid)

    if request.method == "POST":
        s.name = request.POST.get('name')
        s.username = request.POST.get('username')
        s.address=request.POST.get('address')
        s.age=request.POST.get('age')
        s.save()
        messages.info(request, "Profile updated successfully!")
        return redirect('viewprofile')

    return render(request, 'student/editprofile.html', {'m': s})




def forgot(request): 
      if request.method=='POST':
            username=request.POST['username'] 
            data=student.objects.filter(username=username)
            if data.count()>0:
                  request.session["newid"]=data[0].id
                  messages.info(request,'username is found')
                  return redirect('newform')
            
            else:
                  messages.error(request,'username is not found')
              
      return render(request,'student/forgot.html')



def newform(request):
      if request.method=="POST":
            name=request.POST['name']
            age=request.POST['age']
            address=request.POST['address']
            m=student.objects.filter(name=name,age=age,address=address)
            if m.count()>0:
                  return redirect('finalpage')
            else:
                  messages.info(request,'details are not correct')
      return render(request,'student/newform.html')


def finalpage(request):
      if request.method=="POST":
           id=request.session["newid"]
           new_password=request.POST['new_password']
           m=student.objects.filter(id=id).update(password=new_password)
           messages.info(request,'password updated sucessfully')

      return render(request,'student/finalpage.html')




def page1(request):
      return render(request,'student/page1.html')


def page2(request):
      return render(request,'common/page2.html')