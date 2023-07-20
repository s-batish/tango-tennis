from django.contrib import admin
from .models import Lessons


@admin.register(Lessons)
class LessonsAdmin(admin.ModelAdmin):
    list_display = (
        'created_by',
        'level',
        'date',
        'morning',
        'early_afternoon',
        'late_afternoon',
        'evening',
        'created_on',
        'updated_on',
    )
    list_filter = ('level', 'date')
