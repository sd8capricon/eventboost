from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.


# class Account(AbstractUser):
#     is_sponsor = models.BooleanField(null=True)
#     is_organizer = models.BooleanField(null=True)
#     description = models.TextField()

#     def __str__(self):
#         return self.username


class Account(models.Model):
    # org1 event1org
    user = models.OneToOneField(
        User, null=True, on_delete=models.CASCADE, related_name="account"
    )
    is_sponsor = models.BooleanField()
    is_organizer = models.BooleanField()
    description = models.TextField()

    def __str__(self):
        return self.user.username
