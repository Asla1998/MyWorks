from contactsapp import views
from django.urls import path
urlpatterns = [
    path('',views.index,name='index'),
    path('contactsview',views.contactsview,name='contactsview'),
    path('add',views.add,name='add'),
    path('delete/<int:contactid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('edit/<int:id>/',views.edit,name='edit'),




]