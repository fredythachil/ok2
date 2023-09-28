
from django.urls import path, include

from clgapp import views




urlpatterns = [
    path('',views.a,name='a'),
    path('login/',views.loginn,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.logoutt,name='logout'),


    path('', views.StudentListView.as_view(), name='student_changelist'),
    path('add/', views.StudentCreateView, name='student_add'),
    path('<int:pk>/', views.StudentUpdateView.as_view(), name='student_change'),
    path('ajax/load-branches/', views.load_branches, name='ajax_load_branches'),

]







