from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=50, unique=True)
    country = models.CharField(max_length=50, blank=True)
    logo_url = models.URLField(blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Car(models.Model):

    class BodyType(models.TextChoices):
        SEDAN = 'sedan', 'Sedan'
        SUV = 'suv', 'SUV'
        HATCHBACK = 'hatchback', 'Hatchback'
        UTE = 'ute', 'Ute'
        WAGON = 'wagon', 'Wagon'

    class FuelType(models.TextChoices):
        PETROL = 'petrol', 'Petrol'
        DIESEL = 'diesel', 'Diesel'
        HYBRID = 'hybrid', 'Hybrid'
        ELECTRIC = 'electric', 'Electric'

    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='cars')
    model_name = models.CharField(max_length=50)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    body_type = models.CharField(max_length=20, choices=BodyType.choices)
    fuel_type = models.CharField(max_length=20, choices=FuelType.choices)
    seats = models.IntegerField()
    fuel_consumption = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        help_text="Litres per 100km",
    )
    image_url = models.URLField(blank=True)

    class Meta:
        ordering = ['brand__name', 'model_name']

    def __str__(self):
        return f"{self.year} {self.brand.name} {self.model_name}"


class Pro(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='pros')
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text


class Con(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='cons')
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text