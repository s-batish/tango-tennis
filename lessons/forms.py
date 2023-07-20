from django import forms
from .models import Lessons


class AddLessonsForm(forms.ModelForm):
    """
    Form to create lessons
    """
    class Meta:
        model = Lessons
        fields = [
            'level', 'date', 'morning', 'early_afternoon', 'late_afternoon',
            'evening'
        ]
    
    labels = {
        'level': 'Level',
        'date': 'Date',
        'morning': '09:00-11:00',
        'early_afternoon': '12:00-14:00',
        'late_afternoon': '15:00-17-00',
        'evening': '18:00-20:00'
    }