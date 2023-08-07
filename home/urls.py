from django.urls import path
from .views import AddReview, ReviewsList, DeleteReview, EditReview, MyReviews


urlpatterns = [
    path('', ReviewsList.as_view(), name='home'),
    path('my_reviews/', MyReviews.as_view(), name='my_reviews'),
    path('add_review/', AddReview.as_view(), name='add_review'),
    path('delete_review/<slug:pk>/', DeleteReview.as_view(),
         name='delete_review'),
    path('edit_review/<slug:pk>/', EditReview.as_view(),
         name='edit_review'),
]
