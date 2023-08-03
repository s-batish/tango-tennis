from django.urls import path
from .views import AddReview, ReviewsList


urlpatterns = [
    path('', ReviewsList.as_view(), name='home'),
    path('add_review/', AddReview.as_view(), name='add_review'),
]
