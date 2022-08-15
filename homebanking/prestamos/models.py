from django.db import models
import uuid

class Prestamo(models.Model):
    loan_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    loan_payment = models.CharField(max_length=50)
    loan_date = models.DateField()
    loan_total = models.IntegerField()
    customer_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'prestamo'
        