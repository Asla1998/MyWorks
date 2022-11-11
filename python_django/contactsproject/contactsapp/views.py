from django.shortcuts import render,redirect
from .models import ContactsBook

def index(request):
    return render(request,'index.html')


def contactsview(request):
    contact=ContactsBook.objects.all()
    return render(request,'contactlist.html',{'contact':contact})

def add(request):
    contact=ContactsBook.objects.all()
    if request.method=='POST':
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        email=request.POST.get('email')
        phonenumber=request.POST.get('phonenumber')
        address=request.POST.get('address')
        # print(taskname,category,priority,date)
        contact2=ContactsBook(firstname=firstname,lastname=lastname,email=email,phonenumber=phonenumber,address=address)
        # print(task2)
        contact2.save()
    return render(request,'contactlist.html',{'contact':contact})
    
    
def delete(request,contactid):
    contact=ContactsBook.objects.get(id=contactid)
    contact.delete()
    return redirect('contactsview')  


def update(request,id):
    if request.method=="POST":
        add=ContactsBook.objects.get(id=id)
        add.firstname=request.POST["firstname"]
        add.lastname=request.POST["lastname"]
        add.email=request.POST["email"]
        add.phonenumber=request.POST["phonenumber"]
        add.address=request.POST["address"]
        add.save()
        return redirect("contactsview")
 


def edit(request,id):
    contact=ContactsBook.objects.get(id=id)
    return render(request,'updatelist.html',{'contact':contact})






# Create your views here.


# Create your views here.
