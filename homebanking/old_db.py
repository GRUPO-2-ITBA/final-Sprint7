# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
# Unable to inspect table 'cliente'
# The error was: list index out of range


class Cliente(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField()
    customer_subname = models.CharField()
    dob = models.DateField(blank=True, null=True)
    branch_id = models.IntegerField(blank=True, null=True)
    customer_type_id = models.IntegerField(blank=True, null=True)
    address_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'


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


class Direcciones(models.Model):
    address_id = models.AutoField(primary_key=True)
    address_street = models.TextField()
    address_number = models.IntegerField()
    address_city = models.TextField()
    address_province = models.TextField()
    address_country = models.TextField()

    class Meta:
        managed = False
        db_table = 'direcciones'


class Empleado(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=50)
    employee_surname = models.CharField(max_length=50)
    employee_hire_date = models.DateField()
    # Field name made lowercase.
    employee_dni = models.CharField(db_column='employee_DNI', max_length=50)
    branch = models.ForeignKey('Sucursal', models.DO_NOTHING)
    employee_address = models.ForeignKey(
        Direcciones, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empleado'


class MarcaTarjeta(models.Model):
    card_brand_id = models.AutoField(primary_key=True)
    card_brand_description = models.TextField()

    class Meta:
        managed = False
        db_table = 'marca_tarjeta'


class Movimientos(models.Model):
    movimiento_id = models.AutoField(primary_key=True, blank=True, null=True)
    account_id = models.IntegerField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    # This field type is a guess.
    create_at = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movimientos'


class Prestamo(models.Model):
    loan_id = models.AutoField(primary_key=True, blank=True, null=True)
    loan_payment = models.CharField(max_length=50)
    loan_date = models.DateField()
    loan_total = models.IntegerField()
    customer = models.ForeignKey('Cliente', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'prestamo'


class Sucursal(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_number = models.IntegerField()
    branch_name = models.CharField(max_length=50)
    branch_address = models.ForeignKey(
        Direcciones, models.DO_NOTHING, db_column='branch_address')

    class Meta:
        managed = False
        db_table = 'sucursal'


class Tarjeta(models.Model):
    card_id = models.AutoField(primary_key=True)
    card_number = models.CharField(unique=True)
    card_expiration_date = models.TextField()
    card_issue_date = models.TextField()
    card_cvv = models.CharField()
    card_type = models.TextField()
    customer = models.ForeignKey('Cliente', models.DO_NOTHING)
    card_brand_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tarjeta'


class TipoCuenta(models.Model):
    account_type_id = models.AutoField(primary_key=True)
    account_type_description = models.TextField()

    class Meta:
        managed = False
        db_table = 'tipo_cuenta'
