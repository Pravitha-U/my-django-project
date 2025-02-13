from django.contrib import admin
from django.urls import path

from contact import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('signup/',views.signup),
    path('signuppost/',views.signuppost),

    path('login/',views.login),
    path('loginpost/',views.loginpost),

    path('viewprofile/', views.viewprofile),
    path('viewusers/',views.viewusers),

    path('contacts/',views.contacts),
    path('contactspost/', views.contactspost),
    path('viewcontacts/', views.viewcontacts),
    path('editcontacts/<id>', views.editcontacts),
    path('editcontactspost/', views.editcontactspost),

    path('sendcomplaint/',views.sendcomplaint),
    path('sendcomplaintpost/', views.sendcomplaintpost),
    path('deletecontact/<id>', views.deletecontact),
    path('deletecomplaint/<id>', views.deletecomplaint),

    path('searchcontact/', views.searchcontact),
    path('searchcontactpost/', views.searchcontactpost),

    path('viewcomplaints/', views.viewcomplaints),

    path('sendreply/<id>', views.sendreply),
    path('sendreplypost/', views.sendreplypost),
    path('viewreply/', views.viewreply),

    path('editprofile/<id>', views.editprofile),
    path('editprofilepost/', views.editprofilepost),

    path('adminhome/',views.adminhome),

    path('userhome/', views.userhome),

    path('adminviewcontacts/', views.adminviewcontacts),

    path('adminsearchcontacts/',views.adminsearchcontacts),
    path('adminsearchcontactspost/', views.adminsearchcontactspost),

    path('adminsearchusers/', views.adminsearchusers),
    path('adminsearchuserspost/', views.adminsearchuserspost),

    path('adminsearchcomplaintspost/', views.adminsearchcomplaintspost),


]



