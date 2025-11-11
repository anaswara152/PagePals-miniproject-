from django.urls import path
from student import views

urlpatterns=[
    path('',views.home,name='home'),
    path('registration',views.registration,name='registration'),
    path('studenthome',views.studenthome,name='studenthome'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('viewbooks',views.viewbooks,name='viewbooks'),
    path('bookingbook/<int:id>',views.bookingbook,name='bookingbook'),
    path('viewbooking',views.viewbooking,name='viewbooking'),
    path('returnbook/<int:id>',views.returnbook,name='returnbook'),
    path('newpassword',views.newpassword,name='newpassword'),
    path('viewprofile',views.viewprofile,name='viewprofile'),
    path('editprofile',views.editprofile,name='editprofile'),
    path('forgot',views.forgot,name='forgot'),
    path('newform',views.newform,name='newform'),
    path('finalpage',views.finalpage,name='finalpage'),
    path('page1.html',views.page1,name='page1'),
    path('page2',views.page2,name='page2')

]