from django.urls import path, include
from . import views
from django_registration.backends.one_step.views import RegistrationView

urlpatterns=[
    path('',views.karibu, name='karibu'),
    path('welcome/',views.welcome, name='welcome'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', views.logout_user, name='logout'),
]