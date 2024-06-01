
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.home, name='home'),
    path('delete/<int:roll> ' , views.delete_student, name='delete_student')
]
