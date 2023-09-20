from django.db import models
from django.contrib.auth.models import User
class Flower(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='flowers/', null=True, blank=True)
    
    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    flowers = models.ManyToManyField(Flower, through='OrderItem')
    order_date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"Order #{self.id} by {self.customer.name}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.quantity} x {self.flower.name}"

class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    payment_date = models.DateTimeField(auto_now_add=True)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed')])
    
    def __str__(self):
        return f"Payment for Order #{self.order.id}"

class Review(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    review_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Review by {self.customer.name} for {self.flower.name}"

class Cart(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Flower, through='CartItem')
    
    def __str__(self):
        return f"Cart for {self.customer.name}"
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.quantity} x {self.flower.name}"
