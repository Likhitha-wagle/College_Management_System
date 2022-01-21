from django.urls import path
from . import views

urlpatterns = [ 
    path('AddClasses',views.AddClasses.as_view()),
]