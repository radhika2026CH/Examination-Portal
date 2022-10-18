from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

    

# Create your models here.
class Staff(models.Model):
    staff_name = models.CharField(max_length=100, null=False, blank=False)
    phone_number = PhoneNumberField(blank=False, unique=True)
    email = models.EmailField(max_length=254, null=False, blank=False, unique=True)
    active = models.BooleanField(default = True, null= False, blank=False)
    def __str__(self):
        return self.staff_name
    class Meta:
         unique_together = ('phone_number','email')