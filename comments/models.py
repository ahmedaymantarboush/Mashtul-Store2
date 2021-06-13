from django.db import models
from django.utils import timezone

# Create your models here.

class Comment(models.Model):
    """Model definition for Comment."""
    # TODO: Define fields here
    profile = models.ForeignKey("userProfile.Profile", on_delete=models.CASCADE)
    product =  models.ForeignKey("products.Product", on_delete=models.CASCADE)
    comment = models.TextField()
    publishedAt = models.DateTimeField(default=timezone.now )
    
    class Meta:
        """Meta definition for Comment."""
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        """Unicode representation of Comment."""
        return self.profile.user.username

    def get_absolute_url(self):
        """Return absolute url for Comment."""
        return ('Comments')

    # TODO: Define custom methods here
