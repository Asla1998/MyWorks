from todo import views
from django.urls import path
urlpatterns = [
    path('',views.index,name='index'),
    path('todoview',views.todoview,name='todoview'),
    path('add',views.add,name='add'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('edit/<int:id>/',views.edit,name='edit'),




]