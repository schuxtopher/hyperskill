from django.views import View
from django.views.generic.base import TemplateView
from django.http.response import HttpResponse
from django.shortcuts import redirect
from collections import deque

services = {'change_oil': 2,
            'inflate_tires': 5,
            'diagnostic': 30}
line_of_cars = {'change_oil': deque([]),
                'inflate_tires': deque([]),
                'diagnostic': deque([])}
next_ticket = None


class WelcomeView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('<h2>Welcome to the Hypercar Service!</h2>')


class MenuView(TemplateView):
    template_name = 'menu.html'

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
        line_of_cars[service].appendleft(self.ticket_number)
        return context

    def get_minutes_to_wait(self, service):
        if service == 'change_oil':
            minutes_to_wait = (services[service]
                               * (len(line_of_cars['change_oil'])))
            return minutes_to_wait
        elif service == 'inflate_tires':
            minutes_to_wait = (services[service]
                               * (len(line_of_cars['inflate_tires']))
                               + self.get_minutes_to_wait('change_oil'))
            return minutes_to_wait
        elif service == 'diagnostic':
            minutes_to_wait = (services[service]
                               * (len(line_of_cars['diagnostic']))
                               + self.get_minutes_to_wait('inflate_tires'))
            return minutes_to_wait


class ProcessingView(TemplateView):
    template_name = 'processing.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['queue'] = line_of_cars
        return context

    def post(self, request, *args, **kwargs):
        global next_ticket
        next_ticket = self.pop_next_ticket()
        return redirect('/processing')

    @staticmethod
    def pop_next_ticket():
        if line_of_cars['change_oil']:
            return line_of_cars['change_oil'].pop()
        elif line_of_cars['inflate_tires']:
            return line_of_cars['inflate_tires'].pop()
        elif line_of_cars['diagnostic']:
            return line_of_cars['diagnostic'].pop()


class NextView(TemplateView):
    template_name = 'next.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['next_ticket'] = next_ticket
        return context
