from django.urls import path
from . import views

urlpatterns = [ 
    path('AddTeacher',views.AddTeacher.as_view()),
    path('ViewTeacher',views.TeacherView.as_view()),
]