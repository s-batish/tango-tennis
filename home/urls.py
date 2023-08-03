from django.urls import path
from .views import AddReview, ReviewsList, DeleteReview


urlpatterns = [
    path('', ReviewsList.as_view(), name='home'),
    path('add_review/', AddReview.as_view(), name='add_review'),
    path('delete_review/<slug:pk>/', DeleteReview.as_view(),
         name='delete_review'),
]
