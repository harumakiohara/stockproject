from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView, CreateView,FormView

from django.urls import reverse_lazy

from .forms import StockPostForm, ContactForm

from django.utils.decorators import method_decorator

from django.contrib.auth.decorators import login_required

from django.contrib import messages

from django.core.mail import EmailMessage

from .models import StockPost

from django.views.generic import DeleteView, DetailView


class IndexView(ListView):
    template_name = 'index.html'
    queryset = StockPost.objects.order_by('posted_at')
    pahinate_by = 9

@method_decorator(login_required, name='dispatch')

class CreateStockView(CreateView):
   form_class = StockPostForm
   template_name = "post_stock.html"
   success_url = reverse_lazy('stock:post_done')

   def form_valid(self, form):
       postdata = form.save(commit=False)
       postdata.user = self.request.user
       postdata.save()
       return super().form_valid(form)

class PostSuccessView(TemplateView):
    template_name = 'post_success.html'

class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('stock:contact')

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        title = form.cleaned_data['title']
        message = form.cleaned_data['message']
        
        subject = 'お問い合わせ: {}'.format(title)

        message = \
          '送信者名: {0}\nメールアドレス: {1}\n タイトル:{2}\n メッセージ:\n{3}' \
          .format(name, email, title, message)

        from_email = 'xxxxxxxx@gmail.com'
        to_list = ['jyugyou2005@gmail.com']
        message = EmailMessage(subject = subject,
                               body = message,
                               from_email = from_email,
                               to = to_list,
                               ) 
        
        message.send()
        messages.success(
            self.request, 'お問い合わせは正常に送信されました。'
        )
        return super().form_valid(form)

class MypageView(ListView):
    template_name = 'mypage.html'
    paginate_by = 9
    def get_queryset(self):
        queryset = StockPost.objects.filter(
           user = self.request.user).order_by('-posted_at')
        return queryset
    
class DetailView(DetailView):
    template_name = 'detail.html'
    model = StockPost
    
class StockDeleteView(DeleteView):
    model = StockPost
    template_name = 'stock_delete.html'
    success_url = reverse_lazy('stock:mypage')
    def delete(self,request,*args,**kwargs):
        return super().delete(request,*args,**kwargs)

    
