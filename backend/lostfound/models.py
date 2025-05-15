from django.db import models

class LostItem(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('found', 'Found'),
        ('not_found', 'Not Found'),
        ('driver_unreachable', 'Driver Unreachable'),
        ('verified', 'Verified'),
        ('delivered', 'Delivered'),
        ('picked_from_office', 'Picked from Office'),
    ]

    booking_reference_number = models.CharField(max_length=50)
    passenger_mobile_number = models.CharField(max_length=20)
    pickup_address = models.CharField(max_length=255)
    destination_address = models.CharField(max_length=255)
    item_description = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.booking_reference_number} - {self.item_description}"
