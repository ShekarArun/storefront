from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)


class Customer(models.Model):
    MEMBERSHIP_KEY_BRONZE = 'B'
    MEMBERSHIP_KEY_SILVER = 'S'
    MEMBERSHIP_KEY_GOLD = 'G'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_KEY_BRONZE, 'Bronze'),
        (MEMBERSHIP_KEY_SILVER, 'Silver'),
        (MEMBERSHIP_KEY_GOLD, 'Gold'),
    ]

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(
        max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_KEY_BRONZE)


class Order(models.Model):
    PAYMENT_STATUS_KEY_PENDING = 'P'
    PAYMENT_STATUS_KEY_COMPLETE = 'C'
    PAYMENT_STATUS_KEY_FAILED = 'F'

    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_KEY_PENDING, 'Pending'),
        (PAYMENT_STATUS_KEY_COMPLETE, 'Complete'),
        (PAYMENT_STATUS_KEY_FAILED, 'Failed'),
    ]

    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_KEY_PENDING)
