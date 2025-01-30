from django.db import models

# Create your models here.
class Record(models.Model):
    # Cada vez que generemos un registro, este campo generará una marca de tiempo
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email =  models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    addresss = models.CharField(max_length=100)
    city =  models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=20)
    
    # Definimos lo que se verá al momento de ir al panel de administrador.
    def __str__(self):
        return (f"{self.first_name} {self.last_name}")