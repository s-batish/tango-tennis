from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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


class EditLesson(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    View for editing a lesson
    """
    template_name = 'lessons/edit_lessons.html'
    model = Lessons
    form_class = AddLessonsForm
    success_url = '/lessons/our_classes'

    def test_func(self):
        return self.request.user.is_staff


class DeleteLesson(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    View for deleting a lesson
    """
    model = Lessons
    success_url = '/lessons/our_classes'

    def test_func(self):
        return self.request.user.is_staff
