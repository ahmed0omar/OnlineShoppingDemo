from uuid import uuid4
from django.core.validators import MinValueValidator
from django.conf import settings
from django.db import models


# Create your models here.
class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=255)
    unit_price = models.DecimalField(
        max_digits=11,
        decimal_places=2,
        validators=[MinValueValidator(1)])
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['name']


class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE,
                             related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(
               validators=[MinValueValidator(1)])

    class Meta:
        unique_together = [['cart', 'product']]


class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'
    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETE, 'Complete'),
        (PAYMENT_STATUS_FAILED, 'Failed')
    ]
    id = models.UUIDField(primary_key=True, default=uuid4)
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=1, choices=PAYMENT_STATUS_CHOICES,
        default=PAYMENT_STATUS_PENDING)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.PROTECT)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT,
                                related_name='orderitems')
    order = models.ForeignKey(Order, on_delete=models.PROTECT,
                              related_name='items')
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=11, decimal_places=2)

    class Meta:
        unique_together = [['product', 'order']]
