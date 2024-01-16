from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("<str:room>/", views.room, name = "room"),
    path("VerifyData", views.VerifyData, name ="VerifyData"),
    path("storage", views.storage, name = "storage"),
    path("getMessages/<str:room>/", views.getMessages, name = "getMessages"),
    path("register", views.register, name = "register"),
    path("login", views.login, name = "login"),
    path("<str:variable>/logout", views.newlogout, name = "logout"),
    path("logout", views.logout, name = "logouts"),
]