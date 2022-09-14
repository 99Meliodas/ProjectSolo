from django.db import models

class feedback(models.Model):
    

    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=255)
    message = models.TextField()

    def __str_(self):
        return self.name
