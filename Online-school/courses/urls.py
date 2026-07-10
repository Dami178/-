from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.webinar_list, name='webinar_list'),
    path('webinar/<int:pk>/', views.webinar_detail, name='webinar_detail'),
    path('homework/<int:pk>/', views.homework_detail, name='homework_detail'),
    path('curation/', views.curation_list, name='curation_list'),
    path('curation/review/<int:pk>/', views.review_submission, name='review_submission'),
]
