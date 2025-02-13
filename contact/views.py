from datetime import datetime

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from contact.models import *


def signup(request):
    return render(request,'signup.html')

def signuppost(request):
    username=request.POST["username"]
    photo=request.FILES["photo"]
    place=request.POST["place"]
    post=request.POST["post"]
    pin=request.POST["pin"]
    district=request.POST["district"]
    email=request.POST["email"]
    age=request.POST["age"]
    phone=request.POST["phone"]
    gender=request.POST["gender"]
    password=request.POST["password"]

    fs = FileSystemStorage()
    fsave = fs.save(photo.name, photo)


    ob2=Login()
    ob2.username=username
    ob2.password=password
    ob2.type="User"
    ob2.save()

    ob=User()
    ob.username=username
    ob.photo=fsave
    ob.place=place
    ob.post=post
    ob.pin=pin
    ob.district=district
    ob.email=email
    ob.age=age
    ob.phone=phone
    ob.gender=gender
    ob.LOGIN=ob2
    ob.save()
    return HttpResponse("<script>alert('registered successfully');window.location='/contact/login/'</script>")

def login(request):
    return render(request,'loginindex.html')
def loginpost(request):
    user=request.POST["username"]
    pswd=request.POST["password"]
    ob=Login.objects.filter(username=user,password=pswd)
    if ob.exists():
        ob2=Login.objects.get(username=user,password=pswd)
        if ob2.type=="admin":
            return HttpResponse("<script>alert('ok');window.location='/contact/adminhome/'</script>")
        elif ob2.type=="User":
            request.session["lid"]=ob2.id
            return HttpResponse("<script>alert('successfully logged');window.location='/contact/userhome/'</script>")
        else:
            return HttpResponse("<script>alert('user not found');window.location='/contact/login/'</script>")

    else:
         return HttpResponse("<script>alert('invalid user');window.location='/contact/login/'</script>")

def viewprofile(request):
    ob = User.objects.get(LOGIN_id=request.session["lid"])
    return render(request,'viewprofile.html',{"data":ob})

def editprofile(request,id):
    ob=User.objects.get(id=id)
    return render(request,'editprofile.html',{"data":ob})

def editprofilepost(request):
    id=request.POST["id"]
    username=request.POST["username"]
    place=request.POST["place"]
    post=request.POST["post"]
    pin=request.POST["pin"]
    district=request.POST["district"]
    email=request.POST["email"]
    age=request.POST["age"]
    phone=request.POST["phone"]
    gender=request.POST["gender"]

    ob=User.objects.get(id=id)
    ob.username=username
    ob.place=place
    ob.post=post
    ob.pin=pin
    ob.district=district
    ob.email=email
    ob.age=age
    ob.phone=phone
    ob.gender=gender

    if 'photo' in request.FILES:
        photo = request.FILES["photo"]
        fs = FileSystemStorage()
        fsave = fs.save(photo.name, photo)
        ob.photo = fsave

    ob.save()

    return HttpResponse("<script>alert('updated successfully');window.location='/contact/viewprofile'</script>")

def contacts(request):
    return render(request,'contacts.html')

def contactspost(request):
    name=request.POST["name"]
    phone=request.POST["phone"]
    email=request.POST["email"]
    relation=request.POST["relation"]
    photo=request.FILES["photo"]

    fs = FileSystemStorage()
    from datetime import datetime
    date = datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
    fn = fs.save(date, photo)
    path = fs.url(date)

    ob=Contact()
    ob.name=name
    ob.phone=phone
    ob.email=email
    ob.relation=relation
    ob.photo=path
    ob.USER=User.objects.get(LOGIN_id=request.session['lid'])
    ob.save()
    return HttpResponse("<script>alert('ok');window.location='/contact/userhome/'</script>")


def viewcontacts(request):
    ob=Contact.objects.filter(USER__LOGIN_id=request.session["lid"])
    return render(request,'viewcontact.html',{"data":ob})

def editcontacts(request,id):
    ob=Contact.objects.get(id=id)
    return render(request,'editcontacts.html',{"data":ob})
def editcontactspost(request):
    id=request.POST["id"]
    name=request.POST["name"]
    phone=request.POST["phone"]
    email=request.POST["email"]
    relation=request.POST["relation"]

    ob=Contact.objects.get(id=id)
    if 'photo' in request.FILES:
        photo=request.FILES["photo"]
        if photo !="":
            from datetime import datetime
            date = datetime.now().strftime("%Y%%m%d-%H%M%S") + ".jpg"
            fs = FileSystemStorage()
            fsave = fs.save(date, photo)
            path=fs.url(date)
            ob.photo=path


    ob.name=name
    ob.phone=phone
    ob.email=email
    ob.relation=relation
    ob.save()
    return HttpResponse("<script>alert('updated');window.location='/contact/viewcontacts/'</script>")



def deletecontacts(request, id):
    ob = Contact.objects.get(id=id)
    ob.delete()
    return HttpResponse("<script>alert('delete');window.location='/contact/viewcontacts/'</script>")


def sendcomplaint(request):
    return render(request,'sendcomplaint.html')
def sendcomplaintpost(request):
    complaint=request.POST["complaint"]

    ob=Complaint()
    ob.complaint=complaint
    ob.reply="pending"
    ob.date=datetime.now().today()
    ob.USER=User.objects.get(LOGIN_id=request.session["lid"])
    ob.save()
    return HttpResponse("<script>alert('sent');window.location='/contact/viewreply/'</script>")

def viewreply(request):
    if request.session.get('lid'):
        ob=Complaint.objects.filter(USER__LOGIN_id=request.session["lid"])
        return render(request,'viewreply.html',{"data":ob})

def deletecontact(request, id):
    ob = Contact.objects.get(id=id)
    ob.delete()
    return HttpResponse("<script>alert('delete');window.location='/contact/viewcontacts/'</script>")

def deletecomplaint(request,id):
    ob=Complaint.objects.get(id=id)
    ob.delete()
    return HttpResponse("<script>alert('delete');window.location='/contact/viewreply/'</script>")


def viewusers(request):
    object=User.objects.all()
    return render(request,'viewusers.html',{"data":object})

def adminhome(request):
    return render(request,'homeindex.html')

def userhome(request):
    return render(request,'userhomeindex.html')

def viewcomplaints(request):
    object=Complaint.objects.all()
    return render(request,'viewcomplaint.html',{"data":object})


def sendreply(request,id):
    return render(request,'sendreply.html',{"id":id})

def sendreplypost(request):
    id=request.POST['id']
    reply=request.POST["reply"]
    ob=Complaint.objects.get(id=id)
    ob.reply=reply
    ob.save()


    return HttpResponse("<script>alert('sent');window.location='/contact/viewcomplaints/'</script>")

def adminviewcontacts(request):
    object=Contact.objects.all()
    return render(request,'viewcontactadmin.html',{"data":object})

def searchcontact(request):
    return render(request, 'viewcontact.html', {"data": object})

def searchcontactpost(request):
    name=request.POST["name"]
    object = Contact.objects.filter(name__icontains=name)
    return render(request, 'viewcontact.html', {"data": object})

def adminsearchcontacts(request):
    return render(request, 'viewcontact.html', {"data": object})
def adminsearchcontactspost(request):
    name=request.POST["name"]
    object=Contact.objects.filter(name__icontains=name)
    return render(request,'viewcontactadmin.html',{"data":object})

def adminsearchusers(request):
     return render(request, 'viewusers.html',{"data":object})
def adminsearchuserspost(request):
    username=request.POST["username"]
    object=User.objects.filter(username__icontains=username)
    return render(request,'viewusers.html',{"data":object})




def adminsearchcomplaintspost(request):
    date1= request.POST["date1"]
    date2= request.POST["date2"]
    object = Complaint.objects.filter(date__range=[date1,date2])
    return render(request, 'viewcomplaint.html', {"data": object})








