from django.urls import path 
from .views import *
urlpatterns=[
    path('',JobList.as_view(),name='home'),
    path('detail/<int:pk>/',JobDetail.as_view(),name='detail'),
    path('employee_create/',CreateEmployees.as_view(),name='create_employee'),
    path('job_create/',CreateJob.as_view(),name='create_job'),
    path('task_create/',CreateTask.as_view(),name='create_task'),
    path('delete/<int:pk>/',DeleteVacancy.as_view(),name='delete'),
]