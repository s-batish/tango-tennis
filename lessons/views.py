from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Lessons
from .forms import AddLessonsForm


class AddLessons(LoginRequiredMixin, CreateView):
    """
    Add lessons view
    """
    template_name = 'lessons/add_lessons.html'
    model = Lessons
    form_class = AddLessonsForm
    success_url = '/our_classes'

    def form_valid(self, form):
        """
        Automatically names creator from created_by
        """
        form.instance.created_by = self.request.user
        return super(AddLessons, self).form_valid(form)
