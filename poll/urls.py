from django.urls import path
from poll import views

urlpatterns=[
    path('',views.create,name='create'),
    path('poll_list/',views.Homes,name='poll-list'),
    path('Vote/<poll_id>',views.Vote,name='Vote'),
    path('Result/<poll_id>',views.Result,name='result'),
]