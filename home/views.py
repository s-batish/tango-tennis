from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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


class MyReviews(LoginRequiredMixin, ListView):
    """
    View for user to see all their reviews
    """
    template_name = 'home/my_reviews.html'
    model = Review
    context_object_name = 'my_reviews'


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


class EditReview(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    View to edit a review
    """
    template_name = 'home/edit_review.html'
    model = Review
    form_class = ReviewForm
    success_url = reverse_lazy('home')

    # Allows staff to edit any reviews but logged in users can only
    # edit their own
    def test_func(self):
        if self.request.user.is_staff:
            return True
        else:
            return self.request.user == self.get_object().user


class DeleteReview(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    View to delete a review
    """
    model = Review
    success_url = reverse_lazy('home')

    # Allows staff to delete any reviews but logged in users can only
    # delete their own
    def test_func(self):
        if self.request.user.is_staff:
            return True
        else:
            return self.request.user == self.get_object().user
