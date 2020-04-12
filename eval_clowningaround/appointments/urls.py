from rest_framework import routers
from django.urls import include, path

from appointments import views

router = routers.DefaultRouter()
router.register('appointments', views.AppointmentViewSet, basename='appointments')
urlpatterns = [
    path('', include(router.urls)),
    # path('appointments/', views.AppointmentList.as_view()),
    # path('appointments/<int:pk>', views.AppointmentDetail.as_view())
    #path('appointments/<int:pk>', views.appointment_detail)
    # url(r'^$', include(router.urls)),
    # url(r'^api-auth/$', obtain_auth_token, name='api-token-auth'),
    # url(r'^appointment/$', AppointmentView.as_view(), name='appointment'),
    # url(r'^appointment/detail/$', AppointmentDetailView.as_view(), name='appointmen-detail'),
]