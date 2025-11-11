from django.shortcuts import render,redirect,get_object_or_404
from .models import*
from django.contrib import messages
from student.models import*

# Create your views here.
def adminhome(request):
    return render(request,'admin/ahome.html')



def addbook1(request):
     m=category.objects.all()
     if request.method == "POST":
          name=request.POST['name']
          author=request.POST['author']
          numberof_copies=request.POST['numberof_copies']
          categoryid=request.POST['category']
          if len(request.FILES)>0:
               img=request.FILES['file']
          else:
               img="no pic"   
          
          p=book.objects.create(name=name,author=author,coverphoto=img,numberof_copies=numberof_copies,categoryid_id=categoryid)
          p.save()
          messages.info(request,' book added sucessfully')
     s={'m':m}
     return render(request,'admin/addbook.html',s)


def viewbook(request):
     m=book.objects.all()
     p={'m':m}
     return render(request,'admin/viewbook.html',p)

def deletebook(request,id):
    u=book.objects.filter(id=id).delete()
    return redirect('viewbook')  


def editbook(request,id):
     u=get_object_or_404(book,id=id)
     m=category.objects.all()
     if request.method=="POST":
          name=request.POST['name']
          author=request.POST['author']
          numberof_copies=request.POST['numberof_copies']
          categoryid=request.POST['category']
          if 'file' in request.FILES and request.FILES['file']:
            u.coverphoto = request.FILES['file']
          u.name=name
          u.author=author
          u.numberof_copies=numberof_copies
          u.categoryid_id=categoryid
          u.save()
          messages.info(request,"updated sucessfully")
          return redirect('viewbook')
     u=book.objects.filter(id=id) 
     y={'u':u,'m':m}
     return render(request,'admin/editbook.html',y)
 
 
def librarianview(request):
     a=booking.objects.all()
     s={'a':a}
     return render(request,'admin/bookedbooks.html',s)

def acceptbook(request,id):
     abc=get_object_or_404(booking,id=id)
     abc.status='accepted' 
     abc.save()
     books=get_object_or_404(book,id=abc.bookid_id)
     copies=books.numberof_copies
     books.numberof_copies=copies+1
     books.save()
     return redirect('librarianview')


def page3(request):
     return render(request,'admin/page3.html')