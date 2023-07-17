from django.views.generic import TemplateView


class Index(TemplateView):
    """
    View to load page
    """
    template_name = 'home/index.html'
