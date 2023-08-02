from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Review
from .forms import ReviewForm
from django.urls import reverse_lazy


class Index(TemplateView):
    """
    View to load page
    """
    template_name = 'home/index.html'


class AddReview(LoginRequiredMixin, CreateView):
    """
    View to add a review
    """
    template_name = 'home/add_review.html'
    model = Review
    form_class = ReviewForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddReview, self).form_valid(form)
