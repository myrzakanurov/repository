from django.shortcuts import render
from django.views import generic
from . import forms
from django.urls import reverse_lazy


class SignUp(generic.CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/signup.html'


class IndexPage(generic.TemplateView):
    template_name = 'index.html'


class SuccessPage(generic.TemplateView):
    template_name = 'success.html'


class ThanksPage(generic.TemplateView):
    template_name = 'thanks.html'
