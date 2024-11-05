from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10 , decimal_places=2)
    # stock = models.PositiveIntegerField(upload_to='product_images/')

    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField()
    ordered_at = models.DateField(auto_now_add = True)

    def __str__(self):
        return f"Order for {self.product.name}"
