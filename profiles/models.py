from django.db import models
from django.contrib.auth.models import User
from image_optimizer.fields import OptimizedImageField


class userModel(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    Icon = OptimizedImageField(default='avatar.jpg',
                               optimized_image_output_size=(250, 250),
                               optimized_image_resize_method='thumbnail',
                               upload_to="images/")
    username = models.CharField(max_length=25)
    email = models.EmailField(max_length=50)


class pushNotifications(models.Model):
    title = models.CharField(max_length=25)
    body = models.CharField(max_length=50)
    Image = OptimizedImageField(default='avatar.jpg',
                                optimized_image_output_size=(250, 250),
                                optimized_image_resize_method='thumbnail',
                                upload_to="images/")
