from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('alarm', views.alarm, name='alarm'),
    path('view/<str:id>', views.view, name='view'),
    path('delete/<str:id>', views.delete, name='delete'),
    path('delete_image/<str:id>', views.delete_image, name='delete_image')
]
