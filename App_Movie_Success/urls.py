from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views


urlpatterns = [
    path('', views.home, name='home'),
    path('base/', views.base, name='base'),
    path('UserRegisteration/', views.UserRegisteration, name='UserRegisteration'),
    path('Login/', views.Login, name='Login'),
    path('AdminLogin/', views.AdminLogin, name='AdminLogin'),
    path('Predict/', views.Predict, name='Predict'),
    path('AddTrainingData/', views.AddTrainingData, name='AddTrainingData'),
    path('Logout/', views.Logout, name='Logout'),
   

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)