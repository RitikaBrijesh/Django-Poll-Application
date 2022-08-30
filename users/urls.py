from django.urls import path
from .views import home, profile, register, API_object_details, API_objects, register
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', register, name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('api_object/',API_objects.as_view()),
    path('api_detail/<int:pk>',API_object_details.as_view())
]

urlpatterns=format_suffix_patterns(urlpatterns)