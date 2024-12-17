from django.db import models

# Create your models here.
class Municipio(models.Model):
    estado = models.CharField(max_length=100, default='AAAA')
    nome = models.CharField(max_length=200, default='AAAA')

    def __str__(self):
        return f"{self.nome} - {self.estado}"
    
class Queimada(models.Model):
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    risco_fogo = models.DecimalField(max_digits=5, decimal_places=1, default='0.0')
    frp = models.DecimalField(max_digits=5, decimal_places=1, default='0.0') # Fire Radiative Power

    def __str__(self):
        return f"{self.municipio.nome} - Risco Fogo: {self.risco_fogo} - FRP: {self.frp}"
    
class Sugestao(models.Model): 
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return f"{self.nome} - {self.email}"    
