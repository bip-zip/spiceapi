from django.db import models
from product.models import Item
from customer.models import Customer

class Order(models.Model):
    ref_number = models.IntegerField(null=False)
    desc = models.TextField(null=True)
    entry_date = models.DateField(null=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return '{} - {}'.format(self.id, self.ref_number)
    
    # inorder to calculate the total amount
    def calculate_total_amount(self):
        total_amount = sum(
            i.calculate_item_total_amount()
            for i in self.order_items.all()
        )
        return total_amount


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    discount= models.FloatField(null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE,  related_name='order_items')

    def __str__(self) -> str:
        return '{} - {}'.format(self.order.id, self.item.item_name)
    
    def calculate_item_total_amount(self):
        total = self.quantity * self.item.rate
        discount = float((self.discount / 100)*total)
        return total-discount

    
    

    






