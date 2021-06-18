from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
# Create your models here.
class Appointment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    patient_name = models.CharField(max_length=120)
    doctor= models.CharField(max_length=120)
    time = models.TimeField()
    
departments = [('Cardiology', 'Cardiology'), ('Dermatology','Dermatology'), ('Immunology','Immunology'), ('Anesthesiology','Anesthesiology'), ('Emergency', 'Emergency')]
    
class Doctor(models.Model):
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    mobile = models.CharField(max_length=15, null=True)
    department = models.CharField(max_length=50, choices=departments, default = 'Cardiologist')
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return "{} ({})".format(self.name, self.department)