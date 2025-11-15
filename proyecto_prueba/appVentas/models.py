from django.db import models

# Create your models here.
class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'clientes'

class Tienda(models.Model):
    id_tienda = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'tiendas'

class Compra(models.Model):
    id_compra = models.AutoField(primary_key=True)
    fecha = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    
    cliente = models.ForeignKey(
        Cliente,
        on_delete= models.CASCADE,
        db_column='id_cliente',
        related_name='compras'
    )

    tienda = models.ForeignKey(
        Tienda,
        on_delete= models.CASCADE,
        db_column='id_tienda',
    )



    def __str__(self):
        # self.cliente usará automáticamente el __str__ que definimos
        # en el modelo Cliente (o sea, mostrará el nombre).
        return f"Compra #{self.id_compra} de {self.cliente} el {self.fecha}"
    
    class Meta:
        managed = False
        db_table = 'compras'
    