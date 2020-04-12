from rest_framework import generics, viewsets
from .models import Appointment
from .serializers import AppointmentAdminSerializer, AppointmentClientSerializer, AppointmentClownSerializer

# TODO: Appointments must rated by smiley faces
# TODO: Test must be added

"""
Get appointment list and Create appointment
"""


class AppointmentViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.request.user.is_clown:
            return AppointmentClownSerializer
        elif self.request.user.is_client:
            return AppointmentClientSerializer
        elif self.request.user.is_superuser or self.request.user.is_troupe_leader:
            return AppointmentAdminSerializer

    def get_queryset(self):
        if self.request.user.is_clown:
            return Appointment.objects.filter(clown_id=self.request.user.id)
        elif self.request.user.is_client:
            return Appointment.objects.filter(client_id=self.request.user.id)
        elif self.request.user.is_superuser:
            return Appointment.objects.all()
        elif self.request.user.is_troupe_leader:
            return Appointment.objects.filter(created_by_id=self.request.user.id)

# class AppointmentList(generics.ListCreateAPIView):
#
#     def get_serializer_class(self):
#         if self.request.user.is_clown:
#             return AppointmentClownSerializer
#         elif self.request.user.is_client:
#             return AppointmentClientSerializer
#         elif self.request.user.is_superuser or self.request.user.is_troupe_leader:
#             return AppointmentAdminSerializer
#
#     def get_queryset(self):
#         if self.request.user.is_clown:
#             return Appointment.objects.filter(clown_id=self.request.user.id)
#         elif self.request.user.is_client:
#             return Appointment.objects.filter(client_id=self.request.user.id)
#         elif self.request.user.is_superuser:
#             return Appointment.objects.all()
#         elif self.request.user.is_troupe_leader:
#             return Appointment.objects.filter(created_by_id=self.request.user.id)
#
#
# """
# Get appointment detail and Update appointment
# """
#
#
# class AppointmentDetail(generics.RetrieveUpdateDestroyAPIView):
#     def get_serializer_class(self):
#         if self.request.user.is_clown:
#             return AppointmentClownSerializer
#         elif self.request.user.is_client:
#             return AppointmentClientSerializer
#         elif self.request.user.is_superuser or self.request.user.is_troupe_leader:
#             return AppointmentAdminSerializer
#
#     def get_queryset(self):
#         if self.request.user.is_clown:
#             return Appointment.objects.filter(clown_id=self.request.user.id)
#         elif self.request.user.is_client:
#             return Appointment.objects.filter(client_id=self.request.user.id)
#         elif self.request.user.is_superuser:
#             return Appointment.objects.all()
#         elif self.request.user.is_troupe_leader:
#             return Appointment.objects.filter(created_by_id=self.request.user.id)
#

# class AppointmentViewSet(viewsets.ModelViewSet):
#     queryset = Appointment.objects.all()
#     serializer_class = AppointmentSerializers
#     permission_classes = [permissions.IsAuthenticated]

# class AppointmentList(APIView):
#     def get(self, request):
#         if request.user.is_superuser:
#             appointments = Appointment.objects.all()
#             serializer = AppointmentAdminSerializer(appointments, many=True)
#             return Response(serializer.data)
#         elif request.user.is_clown:
#             appointments = Appointment.objects.filter(clown_id=request.user.id)
#             serializer = AppointmentClownSerializer(appointments, many=True)
#             return Response(serializer.data)
#         elif request.user.is_client:
#             appointments = Appointment.objects.filter(client_id=request.user.id)
#             serializer = AppointmentClientSerializer(appointments, many=True)
#             return Response(serializer.data)
#         return Response(status.HTTP_401_UNAUTHORIZED)
#
#     def post(self, request):
#         if request.user.is_superuser:
#             serializer = AppointmentAdminSerializer(data=request.data)
#         elif request.user.is_clown:
#             serializer = AppointmentClownSerializer(data=request.data)
#         elif request.user.is_client:
#             serializer = AppointmentClientSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class AppointmentDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Appointment.objects.get(pk=pk)
#         except Appointment.DoesNotExist:
#             raise Http404
#
# def get_serializer_class(self, request, pk):
#     appointment = self.get_object(pk)
#     if request.user.is_superuser:
#         return AppointmentAdminSerializer(appointment)
#     if request.user.is_clown:
#         return AppointmentClownSerializer(appointment)
#     if request.user.is_client:
#         return AppointmentClientSerializer(appointment)
#
#     def get(self, request, pk):
#         serializer = self.get_serializer_class(request, pk)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         serializer = self.get_serializer_class(request, pk)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         appointment = self.get_object(pk)
#         if request.user.is_superuser:
#             appointment.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def appointment_list(request):
#     if request.method == 'GET':
#         if request.user.is_superuser:
#             appointments = Appointment.objects.all()
#             serializer = AppointmentAdminSerializer(appointments, many=True)
#             return Response(serializer.data)
#         elif request.user.is_clown:
#             appointments = Appointment.objects.filter(clown_id=request.user.id)
#             serializer = AppointmentClownSerializer(appointments, many=True)
#             return Response(serializer.data)
#         elif request.user.is_client:
#             appointments = Appointment.objects.filter(client_id=request.user.id)
#             serializer = AppointmentClientSerializer(appointments, many=True)
#             return Response(serializer.data)
#         return Response(status.HTTP_401_UNAUTHORIZED)
#
#     elif request.method == 'POST':
#         if request.user.is_superuser:
#             serializer = AppointmentAdminSerializer(data=request.data)
#         elif request.user.is_clown:
#             serializer = AppointmentClownSerializer(data=request.data)
#         elif request.user.is_client:
#             serializer = AppointmentClientSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def appointment_detail(request, pk):
#     try:
#         appointment = Appointment.objects.get(pk=pk)
#     except Appointment.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
# if request.method == 'GET':
#     if request.user.is_superuser:
#         serializer = AppointmentAdminSerializer(appointment)
#     elif request.user.is_clown:
#         serializer = AppointmentClownSerializer(appointment)
#     elif request.user.is_client:
#         serializer = AppointmentClientSerializer(appointment)
#     return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         if request.user.is_superuser:
#             serializer = AppointmentAdminSerializer(data=request.data)
#         elif request.user.is_clown:
#             serializer = AppointmentClownSerializer(data=request.data)
#         elif request.user.is_client:
#             serializer = AppointmentClientSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         if request.user.is_superuser:
#             appointment.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# def get_serializer_class(self):
#     if request.user.is_superuser or request.user.is_admin:
#         return AppointmentAdminSerializer(data, many=True)
#     if request.user.is_clown:
#         return AppointmentClownSerializer(data, many=True)
#     if request.user.is_client:
#         return AppointmentClientSerializer(data, many=True)
#     return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
