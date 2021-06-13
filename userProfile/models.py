from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


#Funcions
def uploadTo(instance, filename):
    fileName, ext = filename.split(".")
    return ( f"Users/{str(instance.user.username)}/{str(instance.user.username)}.{ext}" )


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to=uploadTo, max_length=1000, default="/Users/default.jpg",blank=True,null=True)
    address1 = models.CharField(max_length=50, null=True, blank=True)
    address2 =  models.CharField(max_length=50, null=True, blank=True)
    phoneNumber =  models.CharField(max_length=50, null=True, blank=True)
    createdAt = models.DateTimeField(default=timezone.now ,auto_now=False, auto_now_add=False)
    lastLoging = models.DateTimeField(default=timezone.now ,auto_now=False, auto_now_add=False)
    products = models.ManyToManyField("products.Product", related_name='products', blank=True)
    wishes = models.ManyToManyField("products.Product", related_name='wishes', blank=True)
    cart = models.ManyToManyField("products.Product", related_name='cart', blank=True)

    class Meta:
        verbose_name = ("Profile")
        verbose_name_plural = ("Profiles")

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse("Profile_detail", kwargs={"pk": self.pk})

@receiver(post_save, sender=User)
def update_Create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()  
#@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    pass