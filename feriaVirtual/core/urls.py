from django.urls import path
from .views import home, login

#esta url en core se encarga de rutear las views

urlpatterns = [
   path('', home, name="home"),
   path('login', login, name="login"),
]