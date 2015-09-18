from django.shortcuts import render
from django.views.generic import FormView
from .forms import MessageForm, ContactForm


class MessageAddView(FormView):
    template_name = 'contact/message_form.html'
    form_class = ContactForm
    success_url = '/'

    # def form_valid(self, form):
    #     form.save()
    #     return super(MessageAddView, self).form_valid(form)
