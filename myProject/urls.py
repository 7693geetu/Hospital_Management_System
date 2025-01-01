
from django.contrib import admin
from django.urls import path, include
from myApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
   # path('', include('myApp.urls')),
    #path('login.html', views.login, name='login'), 
   # path('login/', LoginView.as_view(template_name='login.html'), name='login'), 
    path('', views.LoginPage, name='login'),
   # path('patient/add', views.ADD_PATIENT, name='add_patient'),
    path('signup/', views.SignupPage, name='signup'),
    #path('login/', views.LoginPage, name='login'),
    path('index/', views.index, name='index'),
    path('logout/', views.LogoutPage, name='logout'),

    path('index.html', views.index, name='index'),
    path('treatment.html', views.treatment, name='treatment'),
    path('about.html', views.about, name='about'),
    path('doctors.html', views.doctors, name='doctors'),
     path('forgot-password/', views.forgot_password, name='forgot-password'),
    path('contact.html', views.contact, name='contact'),
    
    
]