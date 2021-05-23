from django.urls import path
from .views import add, calculations_list

urlpatterns = [
    path("", calculations_list),
    path('add/<int:a>/<int:b>', add),

]