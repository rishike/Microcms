from django.db import models
from django.contrib.sites.models import Site
from django.contrib.auth.models import User

# Create your models here.

# class CustomSite(models.Model):
#     site = models.OneToOneField(Site, on_delete=models.CASCADE, primary_key=True)

class WebPage(models.Model):
    site = models.OneToOneField(Site, on_delete=models.CASCADE, primary_key=True)
    title = models.CharField(max_length=255)
    allowed_devices = models.ManyToManyField('Device')

    def __str__(self):
        return self.title


class PageSection(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='section', blank=True)
    html_content = models.TextField()
    order = models.PositiveIntegerField(default=0, help_text="Enter the order of the section (lower value appears first).")
    page = models.ForeignKey(WebPage, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class Country(models.Model):
    name = models.CharField(max_length=255)
    status = models.BooleanField()

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Vendor(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    managed_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Device(models.Model):
    name = models.CharField(max_length=255)
    device_photo = models.ImageField(upload_to='device')
    currency = models.CharField(max_length=20)
    offer_price = models.DecimalField(max_digits=10, decimal_places=2)
    sourced = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='devices')
    status = models.BooleanField()

    def __str__(self):
        return self.name


class Lead(models.Model):
    LEAD_STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('In-progress', 'In-progress'),
        ('Converted', 'Converted'),
        ('Rejected', 'Rejected'),
    )

    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    referral_code = models.CharField(max_length=10)
    lead_status = models.CharField(max_length=20, choices=LEAD_STATUS_CHOICES)

    def __str__(self):
        return self.name


class WalkIn(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    currency = models.CharField(max_length=20)
    offer_price = models.DecimalField(max_digits=10, decimal_places=2)
    walkin_datetime = models.DateTimeField()
    token_number = models.IntegerField()

    def __str__(self):
        return f"Walk-in {self.id}"
