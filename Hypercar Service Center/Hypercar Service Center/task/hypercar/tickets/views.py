from django.views import View
from django.views.generic.base import TemplateView
from django.http.response import HttpResponse


services = ['Change oil',
            'Inflate tires',
            'Diagnostic']


class WelcomeView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('<h2>Welcome to the Hypercar Service!</h2>')


class MenuView(TemplateView):
    template_name = 'menuPage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = services
        return context
