from typing import Any
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,DetailView,DeleteView

from .forms import EmployeesForm, JobForm, TaskForm 
from .models import *
class JobList(ListView):
    model=Job 
    template_name='job_list.html'
    context_object_name='jobs'
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     jobs = Job.objects.all()
    #     context['jobs'] = jobs
    #     # Create a dictionary to store tasks related to each job
    #     job_tasks = {}
    #     for job in jobs:
    #         # Retrieve all tasks related to the current job
    #         tasks = Task.objects.filter(job=job)
    #         job_tasks[job.id] = tasks
    #     context['tasks'] = job_tasks
    #     return context
    
class JobDetail(DetailView):
    model=Job
    template_name='job_detail.html'
    context_object_name='job'

    def get_context_data(self, **kwargs) :
        context=super().get_context_data(**kwargs)
        
        context['tasks']=Task.objects.filter(job=self.object)
        # context[]=Employee.objects.all()
        return context
    
class CreateEmployees(CreateView):
    model=Employee
    template_name='create_employees.html'
    form_class=EmployeesForm
    success_url=reverse_lazy('home')

class CreateJob(CreateView):
    model=Job
    template_name='create_job.html'
    form_class=JobForm
    success_url=reverse_lazy('home')

class CreateTask(CreateView):
    model=Task
    template_name='create_task.html'
    form_class=TaskForm
    success_url=reverse_lazy('home')

class DeleteVacancy(DeleteView):
    model=Job 
    template_name='delete.html'
    success_url=reverse_lazy('home')
    
