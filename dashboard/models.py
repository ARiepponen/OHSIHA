from django.db import models

class Bond(models.Model):
    description = models.CharField(max_length=200)
    buying_price = models.IntegerField()
    total_price = models.IntegerField()
   

    def __str__(self):
        return self.description
