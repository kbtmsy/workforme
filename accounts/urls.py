from django.urls import path
from .views import LoginConf, Create, Login, Logout, Delete

urlpatterns = [
    path('', LoginConf.as_view(), name='login_conf'),
    path('create/', Create.as_view(), name='create'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('delete/', Delete.as_view(), name='delete'),
]