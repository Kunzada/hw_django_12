from django.db import models
from django.core import validators
from django.core.exceptions import ValidationError
# Create your models here.
def validate_phone_number(value):
    allowed_characters=set("01234567890-() ")
    for char in value:
        if char not in allowed_characters:
            raise ValidationError(
                ('Phone number contains invalid chracters'),
                params={'value':value}
            )

class Employee(models.Model):
    firstName=models.CharField(max_length=20,verbose_name='Имя')
    lastName=models.CharField(max_length=20,verbose_name='Фамилия')
    email=models.CharField(max_length=255,validators=[validators.EmailValidator(message="Email must be from example.com domain")])
    phoneNumber=models.CharField(max_length=20,validators=[validate_phone_number],verbose_name='Номер телефона')
    salary=models.BigIntegerField(verbose_name='Зарплата')

    def __str__(self):
        return f"{self.lastName} {self.firstName}"
    class Meta:
        verbose_name='Работник'
        verbose_name_plural='Работники'

class JobHistory(models.Model):
    startDate=models.DateField()
    endDate=models.DateField()
    class Meta:
        abstract = True

    def clean(self):
        if self.startDate and self.endDate and self.startDate > self.endDate:
            raise ValidationError("Start date cannot be later than end date.")
        
        if self.startDate and self.endDate and self.endDate < self.startDate:
            raise ValidationError("End date cannot be earlier than start date.") 
        
class Job(JobHistory):
    image=models.ImageField(upload_to='job/')
    jobTitle=models.CharField(max_length=255,verbose_name="Название работы")
    minSalary=models.BigIntegerField(verbose_name="Минимальная зарплата")
    maxSalary=models.BigIntegerField(verbose_name="Максимальная зарплата")
    employees=models.ManyToManyField(Employee)

    def __str__(self):
        return self.jobTitle
  
    class Meta:
        verbose_name="Работа"
        verbose_name_plural="Работы"

class Task(models.Model):
    title=models.CharField(max_length=255,verbose_name="Заголовок")
    description=models.TextField(max_length=255,verbose_name="Описание") 
    job=models.ManyToManyField(Job)
    def __str__(self):
        return self.title
  
    class Meta:
        verbose_name="Задача"
        verbose_name_plural="Задачи"
