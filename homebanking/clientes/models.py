from django.db import models


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
