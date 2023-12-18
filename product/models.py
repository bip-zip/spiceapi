from django.db import models

    
class Item(models.Model):

    class Meta():
        verbose_name_plural = 'Products'

    item_name = models.CharField(null=False, max_length = 200)
    rate = models.FloatField(null=False)
    uom=models.CharField(max_length=99, null=True)

    def __str__(self) -> str:
        return '{} - {}'.format(self.id, self.item_name)