from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    pub_date = models.DateField(auto_now=False,auto_now_add=True)
    image = models.ImageField(upload_to = 'images/')
    icon = models.ImageField(upload_to = 'images/')
    body = models.TextField()
    votes_total = models.IntegerField(default=1)
    hunter = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]