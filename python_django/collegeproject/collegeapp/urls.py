from collegeapp import views
from django.urls import path

urlpatterns=[
    path('',views.index,name='index'),
    path('hodhome',views.hodhome,name='hodhome'),
    path('hodpendteacher',views.hodpendteacher,name='hodpendteacher'),

    path('teacherregistration',views.teacherregistration,name='teacherregistration'),
    path('teacherview',views.teacherview,name='teacherview'),
    path('teacherreg',views.teacherreg,name='teacherreg'),

]