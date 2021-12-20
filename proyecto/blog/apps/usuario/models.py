from django.db import models

# Create your models here.
app_name='usuario'
class Usuario(models.Model): 
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=100, blank=False, null=False)
    apellido=models.CharField(max_length=100,blank=False, null=False)
    contrasenia=models.CharField(max_length=50,blank=False, null=False)

    class Meta(): 
        verbose_name='Usuario'
        verbose_name_plural='Usuarios'
    
    def __str__(self): 
        return str(self.id)
