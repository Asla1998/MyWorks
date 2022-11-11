from django.shortcuts import render,redirect
from .models import teacher



def index(request):
    return render(request,'index.html')

def teacherregistration(request):
    return render(request,'teacherreg.html')

def hodhome(request):
    return render(request,'hodhome.html')        

def hodpendteacher(request):
    teacherlist=teacher.objects.all()
    return render(request,'hodpendteacher.html',{'teacherlist':teacherlist})


# teacheradd
def teacherview(request):
    teacherlist=teacher.objects.all()
    return render(request,'teacher.html',{'teacherlist':teacherlist})


def teacherreg(request):
    teacherlist=teacher.objects.all()
    if request.method == 'POST':
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        email=request.POST.get('email')
        department=request.POST.get('department')
        phoneno=request.POST.get('phoneno')
        gender=request.POST.get('gender')
        dob=request.POST.get('dob')
        qualification=request.POST.get('qualification')
        address=request.POST.get('address')
        pin=request.POST.get('pin')
        state=request.POST.get('state')
        country=request.POST.get('country')
        status='0'
        teacherlist1=teacher(firstname=firstname,lastname=lastname,email=email,department=department,phoneno=phoneno,gender=gender,dob=dob,qualification=qualification,address=address,pin=pin,state=state,country=country,status=status)
        teacherlist1.save()
    return render(request,'index.html' ,{'teacherlist':teacherlist})   

#  hod



# Create your views here.
