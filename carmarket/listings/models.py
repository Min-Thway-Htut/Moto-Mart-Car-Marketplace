from django.conf import settings
from django.db import models


class Car(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='car_listings',
    )
    title = models.CharField(max_length=100)
    description =  models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    model  = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    image = models.ImageField(upload_to='car_images/')
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    


