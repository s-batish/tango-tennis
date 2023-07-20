from django.urls import path
from .views import AddLessons


urlpatterns = [
    path('', AddLessons.as_view(), name='add_lessons'),
]
