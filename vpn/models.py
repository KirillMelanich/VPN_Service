from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    age = models.PositiveIntegerField()
    preferences = models.CharField(max_length=63)

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class Site(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    site_name = models.CharField(max_length=255)
    site_url = models.URLField()


class Statistics(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    page_views = models.PositiveIntegerField()
    data_sent = models.PositiveIntegerField()
    data_received = models.PositiveIntegerField()

    def __str__(self):
        return f"Data received: {self.data_received}, data sent: {self.data_sent}, page views: {self.page_views}"


class InternalRoute(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    site_name = models.CharField(max_length=255)
    internal_route = models.CharField(max_length=255)

    def get_absolute_url(self):
        return f"/{self.user.username}/{self.site_name}/{self.internal_route}"
