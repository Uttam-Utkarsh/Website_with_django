from django.db import models

# Create your models here.

class Contact(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Description = models.TextField(default="Nothings Happens")
    added_on = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.Name
    
    class Meta:
        verbose_name =  "Contact Table"