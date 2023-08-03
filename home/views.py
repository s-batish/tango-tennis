from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Review
from .forms import ReviewForm
from django.urls import reverse_lazy
from django.contrib import messages


class ReviewsList(ListView):
    """
    View to see all reviews
    """
    template_name = 'home/index.html'
    model = Review
    context_object_name = 'reviews'


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
        messages.add_message(
            self.request, messages.SUCCESS, 'Your review has been saved!')
        return super(AddReview, self).form_valid(form)
