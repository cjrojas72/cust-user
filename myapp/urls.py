from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.loginview, name="login"),
    path('logout/', views.loginview),
    path('signup/', views.signUpview)
]
