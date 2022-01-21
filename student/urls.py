from django.urls import path
from . import views

urlpatterns = [ 
    path('AddStudent',views.AddStudent.as_view()),
    path('ViewStudent',views.StudentView.as_view()),
]