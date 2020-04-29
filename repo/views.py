from django.shortcuts import render, redirect
from repo.models import Data
from django.views import generic
from repo import forms
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
User = get_user_model()


class RepoUpload(LoginRequiredMixin, generic.CreateView):
    form_class = forms.RepoFileUploadForm
    template_name = 'repo/file_upload.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class DocumentListView(generic.ListView):
    template_name = 'repo/document_list.html'
    model = Data
    context_object_name = 'documents'


class DocumentDetailView(generic.DetailView):
    model = Data
    context_object_name = 'documents_detail'
    template_name = 'repo/document_detail.html'
