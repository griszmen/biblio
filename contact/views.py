from django.shortcuts import render
from django.views.generic import FormView
from .forms import MessageForm


class MessageAddView(FormView):
    from_class = MessageForm
    template_name = 'contact/message_form.html'
