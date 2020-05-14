
from django.urls import path
import views.allblogs

urlpatterns = [

    path('', views.allblogs, name='allblogs'),

]
