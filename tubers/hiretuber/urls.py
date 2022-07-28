from django.urls import path 

from  . import views


urlpatterns = [
   path('hiretuber',views.hiretuber,name='hiretuber'),
   path('<int:id>',views.youtubers_detail,name="youtubers_detail"),
]