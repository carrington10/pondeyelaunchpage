from django.db import models

class Email(models.Model):
      email = models.CharField(max_length=255)
      def __str__(self):
          return self.email
