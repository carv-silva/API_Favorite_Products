from django.db import models
from .validation import check_product_existence

class Customer(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Favorite(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product_id = models.CharField(max_length=200,validators=[check_product_existence])

    class Meta:
        ordering = ['customer']
        unique_together = ('customer', 'product_id')

    @property
    def url(self):
        return f'http://challenge-api.luizalabs.com/api/product/{self.product_id}/'

    def __str__(self):
        return f'{self.customer.name} - {self.product_id}'