from django.urls import path
from .views import AddLessons, OurClassesView


urlpatterns = [
    path('add_lessons/', AddLessons.as_view(), name='add_lessons'),
    path('our_classes/', OurClassesView.as_view(), name='our_classes'),
]
