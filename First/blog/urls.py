from django.urls import path
from .views import homePage
from . import views



urlpatterns = [
    # 
    path("",homePage, name="homepage"),
    path('employee/',views.employee_data, name="home")
]