from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Lessons
from .forms import AddLessonsForm


class OurClassesView(ListView):
    """
    View all classes
    """
    template_name = 'lessons/our_classes.html'
    model = Lessons
    context_object_name = 'lessons'


class AddLessons(LoginRequiredMixin, CreateView):
    """
    Add lessons view
    """
    template_name = 'lessons/add_lessons.html'
    model = Lessons
    form_class = AddLessonsForm
    success_url = '/lessons/our_classes'

    def form_valid(self, form):
        """
        Automatically names creator from created_by
        """
        form.instance.created_by = self.request.user
        return super(AddLessons, self).form_valid(form)
