from django.urls import path

from . import views
urlpatterns = [
    path('CreatAccount', views.CreatAccount, name='CreatAccount'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('forgetPassword', views.forgetPassword, name='forgetPassword'),
    path('transections', views.transections, name='transections'),
    path('cred', views.cred, name='cred'),
    path('creditcardForm', views.creditcardForm, name='creditcardForm'),
    path('contactUs', views.contactUs, name='contactUs'),

]
