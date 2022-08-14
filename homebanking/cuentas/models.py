from django.db import models

# Create your models here.
class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True, blank=True)
    customer = models.ForeignKey('Cliente', models.DO_NOTHING)
    balance = models.IntegerField()
    iban = models.TextField()
    account_type = models.ForeignKey(
        'TipoCuenta', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuenta'
        

class TipoCuenta(models.Model):
    account_type_id = models.AutoField(primary_key=True)
    account_type_description = models.TextField()

    class Meta:
        managed = False
        db_table = 'tipo_cuenta'
        
        
class Cliente(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.TextField()
    customer_subname = models.TextField()
    dob = models.DateField(blank=True, null=True)
    branch_id = models.IntegerField(blank=True, null=True)
    customer_type_id = models.IntegerField(blank=True, null=True)
    address_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'
        