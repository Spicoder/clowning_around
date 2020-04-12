from rest_framework import serializers

from .models import Appointment
from clowning_around.users.models import Clown, Client


class ClownSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clown
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class AppointmentAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'
        read_only_fields = ['rating', 'status', 'report', 'request']


class AppointmentClownSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = [
            'client_id',
            'created_by_id',
            'date_of_appointment',
            'status',
            'report',
            'request'
        ]

        read_only_fields = ['client_id', 'created_by_id', 'date_of_appointment']


class AppointmentClientSerializer(serializers.ModelSerializer):
    # def __init__(self, *args, **kwargs):
    #     super(AppointmentClientSerializer, self).__init__(*args, **kwargs)
    #
    #     request = kwargs['context']['request']
    #     current_status = request.GET.get('status', False)
    #     print(request.GET.get('rating', False))
    #
    #     if current_status == 'completed':
    #         self.fields['rating'].read_only = True
    # TODO: Allow Client to update rating if status is completed
    class Meta:
        model = Appointment
        fields = [
            'client_id',
            'created_by_id',
            'date_of_appointment',
            'status',
            'rating',
            'report',
            'request'
        ]

        read_only_fields = ['clown_id', 'created_by_id', 'date_of_appointment', 'report',
                            'request', 'status']

    def update(self, instance, validated_data):
        instance.date_of_appointment = validated_data.get('date_of_appointment', instance.date_of_appointment)
        instance.request = validated_data.get('request', instance.request)
        instance.report = validated_data.get('report', instance.report)
        instance.created_by_id = validated_data.get('created_by_id', instance.created_by_id)
        instance.client_id = validated_data.get('client_id', instance.client_id)
        instance.status = validated_data.get('status', instance.status)
        print(instance.status)
        if instance.status == 'completed':
            instance.rating = validated_data.get('rating', instance.rating)
        instance.save()
        return instance
WW