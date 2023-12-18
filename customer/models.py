from django.db import models

class Customer(models.Model):
    name = models.CharField(null=False, max_length=99)
    email = models.EmailField(null=True, blank=True)
    contact = models.CharField(null=False, max_length=10)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    
