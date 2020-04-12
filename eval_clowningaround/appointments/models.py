from django.db import models
from django.contrib.auth.models import AbstractUser

from clowning_around.users.models import Clown, Client, TroupeLeader

# Create your models here.

# Appointments status selected by clowns
Status_choices = (
    ('upcoming', "upcoming appointments"),
    ('incipient', "incipient appointments"),
    ('completed', "completed appointments"),
    ('cancelled', "cancelled appointments"),
)

# Appointments rates by clients
Rates_choices = (
    (1, "Very Bad"),
    (2, "Bad"),
    (3, "Good"),
    (4, "Very Good"),
    (5, "Excellent")
)


class Appointment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='appointment_client')
    clown = models.ForeignKey(Clown, on_delete=models.CASCADE, related_name='appointment_clown')
    created_by = models.ForeignKey(TroupeLeader, on_delete=models.CASCADE)
    date_of_appointment = models.DateField()
    rating = models.IntegerField(null=True, choices=Rates_choices)
    status = models.CharField(max_length=20, choices=Status_choices, default='upcoming')
    report = models.TextField(max_length=800, blank=True, default='')
    request = models.TextField(max_length=800, blank=True, default='')

    def __str__(self):
        return str(self.clown)
