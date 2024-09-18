from django.db import models
from django.contrib.auth.models import User

class Donor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=3)
    age = models.PositiveIntegerField()
    location = models.Charfield(max_length=100)
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.user.username} ({self.blood_group})'

class BloodRequest(models.Model):
    patient_name=models.CharField(max_length=100)
    blood_group = models.CharField(max_length=3)
    quantity = models.DecimalField(max_digits=5, decimal_places=2)
    hospital = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    request_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.patient_name} ({self.blood_group})'

class Donation(models.Model):
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return f'{self.donor} -> {self.blood_request}'


