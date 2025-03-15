from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_certificate, name='upload_certificate'),
    path('certificates/', views.student_certificates, name='student_certificates'),
    path('certificate_list/', views.certificate_list, name='certificate_list'),
    path('approve/<int:cert_id>/', views.approve_certificate, name='approve_certificate'),
]
