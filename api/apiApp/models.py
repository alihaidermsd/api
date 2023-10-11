from django.db import models



class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80)
    location = models.CharField(max_length=250)
    about = models.TextField()
    COMPANY_TYPES = (
        ('IT', 'IT'),
        ('Non IT', 'Non IT'),
        ('Mobile phones', 'Mobile phones'),
    )
    type = models.CharField(max_length=100, choices=COMPANY_TYPES)
    added_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name + '  :  ' + self.location
    


class Employee(models.Model):
    name= models.CharField(max_length=100)
    email= models.CharField(max_length=200)
    address= models.CharField(max_length=200)
    phone= models.CharField(max_length=200)
    about= models.TextField()
    Employee_TYPES =(
        ('Manager','manager'),
        ('software Dev','soft dev'),
        ('Project Leader','pl'),
    )
    position = models.CharField(max_length=100, choices=Employee_TYPES)

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
