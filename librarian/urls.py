from django.urls import path
from librarian import views


urlpatterns=[
    path('adminhome',views.adminhome,name='adminhome'),
    path('addbook1',views.addbook1,name='addbook1'),
    path('viewbook',views.viewbook,name='viewbook'),
    path('deletebook/<int:id>',views.deletebook,name='deletebook'),
    path('editbook/<int:id>',views.editbook,name='editbook'),
    path('librarianview',views.librarianview,name='librarianview'),
    path('acceptbook/<int:id>',views.acceptbook,name='acceptbook'),
    path('page3',views.page3,name='page3')

]