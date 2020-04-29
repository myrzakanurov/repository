from django.urls import path
from . import views

app_name = 'repo'

urlpatterns = [
    path('add/', views.RepoUpload.as_view(), name='add'),
    path('all/', views.DocumentListView.as_view(), name='all'),
    path('all/<int:pk>/', views.DocumentDetailView.as_view(), name='detail'),
]
