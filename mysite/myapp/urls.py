from django.urls import path
from .views import homapage , Login , Register ,logout_view

urlpatterns = [
    path('',homapage),
    path('accounts/login/',Login),
    path('register',Register),
    path('logout',logout_view)
]
