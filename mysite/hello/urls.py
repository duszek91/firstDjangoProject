from django.urls import path

from . import views

urlpatterns = [

    path('', views.hello),
    path('<int:name>/', views.hello),

]
