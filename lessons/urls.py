from django.urls import path
from .views import AddLessons, OurClassesView, DeleteLesson


urlpatterns = [
    path('add_lessons/', AddLessons.as_view(), name='add_lessons'),
    path('our_classes/', OurClassesView.as_view(), name='our_classes'),
    path('delete_lesson/<slug:pk>/', DeleteLesson.as_view(), name='delete_lesson')
]
