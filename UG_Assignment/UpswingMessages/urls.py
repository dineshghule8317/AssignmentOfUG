from .views import StatusCountView
from django.urls import path

urlpatterns = [
    path('status/', StatusCountView.as_view(), name='status_count'),
]