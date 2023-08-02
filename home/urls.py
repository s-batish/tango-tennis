from django.urls import path
from .views import Index, AddReview, ReviewsList


urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('add_review/', AddReview.as_view(), name='add_review'),
    path('', ReviewsList.as_view(), name='reviews')
]
