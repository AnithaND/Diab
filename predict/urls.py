from django.urls import path
from .import views
urlpatterns=[
    path('',views.home_page,name='loginpage'),
    path('login/',views.login,name='loginpage'),
    path('home/',views.home,name='homepage'),
    path('register/',views.register,name='registerpage'),
    path('success/',views.success,name='loginpage'),
    path('saveuser/',views.saveuser),
    path('verifyuser/',views.verifyuser),
    path('result/',views.result)
]