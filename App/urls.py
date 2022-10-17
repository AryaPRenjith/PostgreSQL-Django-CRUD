from django.urls import path
from .import views


urlpatterns=[ 
    path('',views.showemp ,name='showemp'),
    path('insert',views.insertemp , name='insertemp'),
    path('edit/<int:id>',views.editemp , name='edit'),
    path('update/<int:id>',views.updateemp, name='updateemp'),
    path('Delete/<int:id',views.delemp,name='delemp')
]