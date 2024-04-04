from email import message

from django.conf.global_settings import EMAIL_HOST_USER
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.core import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView,View
from django.views.generic.edit import UpdateView, DeleteView



from app_news.models import News


# Create your views here.
class AddNewsView(LoginRequiredMixin, CreateView):
    template_name = 'news/add_news.html'
    model = News
    success_url = reverse_lazy('home')
    fields = ['news_title', 'news_description', 'news_image', 'news_content', 'news_category']
    
    def form_valid(self, form):
        form.instance.news_author = self.request.user
        return super().form_valid(form)


class ListNewsView(ListView):
    template_name = 'news/list_news.html'
    model = News
    paginate_by = 2
    # context_object_name = 'xabar'


class DetailNewsView(DetailView):
    template_name = 'news/show_news.html'
    model = News





class NewsUpdateView(LoginRequiredMixin, UpdateView):
    model = News
    fields = ['news_title', 'news_description', 'news_image', 'news_content', 'news_category'] 
    template_name = 'news/update_news.html'
    success_url = reverse_lazy('home')

class NewsDeleteView(LoginRequiredMixin, DeleteView):
    model = News
    template_name = 'news/delete_news.html'  # HTML-malumotlar manbani nomi
    success_url = reverse_lazy('home')  # O'chirish muvaffaqiyatli amalga oshirildiqdan keyin qayerga qaytish kerakligi


class SuperuserRequiredMixin (UserPassesTestMixin):
    def __init__(self):
        self.request = None

    def test_func(self):
        return self.request.user.is_superuser


class SendEmailView(SuperuserRequiredMixin, LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        return render(request, template_name='news/send_email.html')

def post(self, request, *args, **kwargs):
    subject = request.POST.get('subject')
    message=request.POST.get('message')

    users=User.objects.all()
    for user in users:
        recipient_list = [user.email]
        send_mail(subject, message, EMAIL_HOST_USER, recipient_list)
        return render(request, template_name='news/send_email.html')

 
class SendEmailsView(View):

    def get(self, request, *args, **kwargs):
        return render(request, template_name='news/send_emails.html')







