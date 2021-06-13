from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

#Funcions
def uploadTo(instance, filename):
    fileName, ext = filename.split(".")
    return ( f"Products/{str(instance.category)}/{str(instance.publisher)}/{str(instance.name)}/{str(instance.name)}.{ext}" )

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Category_detail", kwargs={"pk": self.pk})

class Unit(models.Model):
    """Model definition for Unit."""
    # TODO: Define fields here
    name = models.CharField(max_length=50)

    class Meta:
        """Meta definition for Unit."""
        verbose_name = 'Unit'
        verbose_name_plural = 'Units'

    def __str__(self):
        """Unicode representation of Unit."""
        return self.name


class Product(models.Model):
    order_key = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField(default=0)
    sale = models.FloatField(default=0)
    quantity = models.FloatField(default=0)
    sold = models.FloatField(default=0)
    unit = models.ForeignKey("Unit", on_delete=models.CASCADE, related_name='unit',default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category',default=0)
    rate = models.FloatField(default=0)
    raters = models.ManyToManyField(User, blank=True)
    publisher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='publisher')
    publishedAt = models.DateField(default=timezone.now )
    image = models.ImageField(upload_to=uploadTo, default="/Products/default.jpg")

    class Meta:
        verbose_name = ("Product")
        verbose_name_plural = ("Products")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Product_detail", kwargs={"pk": self.pk})