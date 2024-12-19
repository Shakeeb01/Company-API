from django.db import models



# Company Model
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=100,choices=(
        ('IT','IT'),
        ('Non IT','Non IT'),
        ('Mobiles Phones','Mobiles Phones'),
    ))
    added_date = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name + ' -- ' + self.location


# Employee Model
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    phone_Number = models.CharField(max_length=15)
    about = models.CharField(max_length=100)
    position = models.CharField(max_length=50,choices=(
        ('Manager','MN'),
        ('Software Developer','SD'),
        ('Project Lead','PL'),
        ('Quality Assurence','QA'),
    ))
    company = models.ForeignKey(Company,on_delete=models.CASCADE,related_name='employees')
    
   
   