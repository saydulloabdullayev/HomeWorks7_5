from django.urls import path

from .views import (
    AddNewsView,
    ListNewsView,
    DetailNewsView, 
    NewsUpdateView, 
    NewsDeleteView,
    SendEmailView,
    SendEmailsView,
)

urlpatterns = [
    path('add/', AddNewsView.as_view(), name='add_news'),
    path('<int:pk>/', DetailNewsView.as_view(), name='show_news'),
    path('', ListNewsView.as_view(), name='list_news'),
    path('edit/<int:pk>/', NewsUpdateView.as_view(), name='update_news'),
    path('delete/<int:pk>/', NewsDeleteView.as_view(), name='delete_news'),
    path('send/', SendEmailView.as_view(), name='send_email'),
    path('send_mails/', SendEmailsView.as_view(), name='send_emails')
]


