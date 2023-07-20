from django.view.generic import CreateView
from .models import Lessons
from .form import AddLessonsForm


class AddLessons(CreateView):
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
