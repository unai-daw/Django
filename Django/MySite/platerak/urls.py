from django.urls import path
from . import views

urlpatterns = [
    path('', views.platerakHTML, name='platerakHTML'),
    path('addPlat/', views.addPlat, name='addPlat'),
    path('addPlat/addrecord/', views.addrecord, name='addrecord'),
    path('deletePlat/<int:id>', views.deletePlat, name='deletePlat'),
    path('updatePlat/<int:id>', views.updatePlat, name='updatePlat'),
    path('updatePlat/updaterecordPlat/<int:id>', views.updaterecordPlat, name='updaterecordPlat'),
    path('sumaPlat/', views.sumaPlat, name='sumaPlat'),
    path('calcusumPlat/', views.calcusumPlat, name='calcusumPlat'),
]