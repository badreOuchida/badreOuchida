from django.urls import path
from .views import homapage , Login , Register ,logout_view ,Switch ,details  ,ApplyView,Accepte,Remove

urlpatterns = [
    path('',homapage ,name="home"),
    path('accounts/login/',Login , name="login"),
    path('register',Register , name='register'),
    path('logout',logout_view , name="logout"),
    path('switch',Switch , name="switch"),
    path('de',details , name="de"),
    path('apply',ApplyView , name="apply"),
    path('accept/<str:pk>',Accepte , name="accpt"),
    path('remove/<str:pk>',Remove , name="remove"),
]
