from django.shortcuts import render,redirect
from .models import TodoTask

def index(request):
    return render(request,'index.html')


def todoview(request):
    task=TodoTask.objects.all()
    return render(request,'task.html',{'task':task})

def add(request):
    task=TodoTask.objects.all()
    if request.method=='POST':
        taskname=request.POST.get('taskname')
        category=request.POST.get('category')
        priority=request.POST.get('priority')
        date=request.POST.get('date')
        print(taskname,category,priority,date)
        task2=TodoTask(taskname=taskname,category=category,priority=priority,date=date)
        print(task2)
        task2.save()
    return render(request,'task.html',{'task':task})
    
    
def delete(request,taskid):
    task=TodoTask.objects.get(id=taskid)
    task.delete()
    return redirect('todoview')  


def update(request,id):
    if request.method=="POST":
        add=TodoTask.objects.get(id=id)
        add.taskname=request.POST["taskname"]
        add.category=request.POST["category"]

        add.priority=request.POST["priority"]
        add.date=request.POST["date"]
        add.save()
        return redirect("todoview")
 


def edit(request,id):
    task=TodoTask.objects.get(id=id)
    return render(request,'update.html',{'task':task})






# Create your views here.
