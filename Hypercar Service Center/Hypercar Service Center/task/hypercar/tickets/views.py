from django.views import View
from django.views.generic.base import TemplateView
from django.http.response import HttpResponse


services = {'change_oil': 2,
            'inflate_tires': 5,
            'diagnostic': 30}
line_of_cars = {'change_oil': [],
                'inflate_tires': [],
                'diagnostic': []}


class WelcomeView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('<h2>Welcome to the Hypercar Service!</h2>')


class MenuView(TemplateView):
    template_name = 'menuPage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = services.keys()
        return context


class TicketView(TemplateView):
    template_name = 'ticket.html'
    ticket_number = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        TicketView.ticket_number += 1
        self.ticket_number = TicketView.ticket_number

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        service = kwargs['service']
        context['service'] = service
        context['ticket_number'] = self.ticket_number
        context['minutes_to_wait'] = self.get_minutes_to_wait(service)
        line_of_cars[service].append(self.ticket_number)
        return context

    def get_minutes_to_wait(self, service):
        if service == 'change_oil':
            minutes_to_wait = services[service] * (len(line_of_cars['change_oil']))
            return minutes_to_wait
        elif service == 'inflate_tires':
            minutes_to_wait = services[service] * (len(line_of_cars['inflate_tires']))
            queue = self.get_minutes_to_wait('change_oil')
            return minutes_to_wait + queue
        elif service == 'diagnostic':
            minutes_to_wait = services[service] * (len(line_of_cars['diagnostic']))
            queue = self.get_minutes_to_wait('inflate_tires')
            return minutes_to_wait + queue
