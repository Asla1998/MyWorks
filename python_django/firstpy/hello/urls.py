from hello import views
from django.urls import path
urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('login',views.login,name='login'),
    path('registration',views.registration,name='registration')


]