from django.db import models

class News(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.URLField()
    external_link = models.URLField()
    
    def __str__(self):
        return self.title
