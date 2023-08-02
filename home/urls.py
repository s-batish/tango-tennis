from django.urls import path
from .views import Index, AddReview


urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('add_review/', AddReview.as_view(), name='add_review')
]