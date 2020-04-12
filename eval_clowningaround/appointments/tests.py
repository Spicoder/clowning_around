from django.test import TestCase
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

# automated
# new / blank db

from appointments.models import Appointment
from clowning_around.users.models import Clown, Troupe, Client, TroupeLeader

User = get_user_model()


class AppointmentAPITestCase(APITestCase):
    def setUp(self):
        user_clown = User(
            name='testcase',
            username='testuser',
            email='test@test.com',
            is_clown=True)
        user_clown.set_password("somerandpass")
        user_clown.save()

        user_client = User(
            name='testclient',
            username='testclientuser',
            email='client@test.com',
            is_client=True)
        user_client.set_password("clientpassword")
        user_client.save()

        user_troupe = User(
            name='testtroupe',
            username='testtroupe_username',
            email='troupe@test.com',
            is_troupe_leader=True)
        user_troupe.set_password("sometroupepassword")
        user_troupe.save()

        troupe_instance = Troupe.objects.create(
            name='troupeTest',
            max_capacity=2
        )

        clown_instance = Clown.objects.create(
            user=user_clown,
            rank=2,
            troupe=troupe_instance
        )

        client_instance = Client.objects.create(
            user=user_client,
            contact_name='test_client',
            contact_email='test@client.com',
            contact_number='contactname'
        )

        troupe_instance = TroupeLeader.objects.create(
            user=user_troupe,
            troupe=troupe_instance
        )

        appointment_instance = Appointment.objects.create(
            client=client_instance,
            clown=clown_instance,
            created_by=troupe_instance,
            date_of_appointment='2020-05-08',
            rating=2,
            status='completed',
            report="This is a test"
        )

    def test_single_user(self):
        user_count = User.objects.count()
        self.assertEqual(user_count, 3)

    def test_single_troupe(self):
        troupe_count = Troupe.objects.count()
        self.assertEqual(troupe_count, 1)

    def test_single_clown(self):
        clown_count = Clown.objects.count()
        self.assertEqual(clown_count, 1)

    def test_single_client(self):
        client_count = Clown.objects.count()
        self.assertEqual(client_count, 1)

    def test_single_appointment(self):
        appointment_count = Appointment.objects.count()
        self.assertEqual(appointment_count, 1)

    def test_single_troupe(self):
        troupe_count = Appointment.objects.count()
        self.assertEqual(troupe_count, 1)

# Create your tests here.
