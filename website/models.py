from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Customer Reviews model
class Review(models.Model):
    review_id = models.CharField(max_length=50)
    review_rating = models.IntegerField()
    review_comments = models.CharField(max_length=500)
    review_image = models.ImageField(upload_to='review_images/', null=True, blank=True)
    service_id = models.ForeignKey('Service', on_delete=models.RESTRICT, null=True)


# Services that are offered
class Service(models.Model):
    service_id = models.CharField(max_length=50)
    service_title = models.CharField(max_length=200)
    service_info = models.CharField(max_length=200)
    service_cost = models.CharField(max_length=200)
    service_img = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.service_title

    def get_absolute_url(self):
        """Returns the URL to access a particular author instance."""
        return reverse('service_detail', args=[str(self.id)])


class ServiceRequest(models.Model):
    contact_ID = models.CharField(max_length=50)
    contact_first_name = models.CharField(max_length=200)
    contact_last_name = models.CharField(max_length=200)
    contact_preferredService = models.CharField(max_length=200)
    usr_id = models.ForeignKey(User, on_delete=models.RESTRICT, null=True)


# Invoice model
class Invoice(models.Model):
    invoice_no = models.CharField(max_length=50)
    invoice_date = models.CharField(max_length=200)
    invoice_total = models.CharField(max_length=200)
    invoice_description = models.CharField(max_length=200)
    service_id = models.ForeignKey('Service', on_delete=models.RESTRICT, null=True)


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publish_date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='blog_photos/', null=True, blank=True)

    def __str__(self):
        return self.title
