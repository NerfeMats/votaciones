from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


#model





class Votante(models.Model):
    
    email = models.EmailField(unique=True)
    
     

    class Meta:
        verbose_name = "Votante"
        verbose_name_plural = "Votantes"

    def __str__(self):
        return self.email



class PartidoPolitico(models.Model):
    
    
    nombrePP =models.CharField(max_length=50)
    logo = models.ImageField()  #pip install Pillow
    

    class Meta:
        verbose_name = "PartidoPolitico"
        verbose_name_plural = "PartidoPoliticos"

    def __str__(self):
        return self.nombrePP

    # def get_absolute_url(self):
    #     return reverse("PartidoPolitico_detail", kwargs={"pk": self.pk})



class Votacion(models.Model):
    
    partidopolitico = models.ForeignKey(PartidoPolitico, on_delete=models.CASCADE)
    numerodevotos = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Votacion"
        

    def __str__(self):
        return self.partidopolitico.nombrePP

@receiver(post_save,sender = PartidoPolitico)
def actulizaprescripciondemedicamento(sender, instance, **kwargs):
    # print(instance)
    Votacion.objects.create(partidopolitico=instance)
    
    