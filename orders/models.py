from django.db import models

class Customer(models.Model):
    name = models.CharField(null=False, max_length=99)
    email = models.EmailField(null=True, blank=True)
    contact = models.CharField(null=False, max_length=10)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    

class Order(models.Model):
    ref_number = models.IntegerField(null=False)
    desc = models.TextField(null=True)
    entry_date = models.DateField(null=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return '{} - {}'.format(self.id, self.ref_number)
    
    
class OrderItem(models.Model):
    item_name = models.CharField(null=False, max_length = 200)
    quantity=models.PositiveIntegerField(default=1)
    discount= models.FloatField(null=True)
    rate = models.FloatField(null=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return '{} - {}'.format(self.order.id, self.item_name)

    






