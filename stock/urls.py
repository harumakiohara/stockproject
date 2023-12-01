from django.urls import path
from . import views
app_name = 'stock'

urlpatterns = [
    path('',views.IndexView.as_view(), name = 'index'),
    path('post/',views.CreateStockView.as_view(),name='post'),
    path('post_done/',
         views.PostSuccessView.as_view(),
         name = 'post_done'),
    path('contact/',
         views.ContactView.as_view(),
         name = 'contact'),
    path('mypage/',views.MypageView.as_view(), name = 'mypage'),
    path('stock-detail/<int:pk>',
         views.DetailView.as_view(),
         name = 'stock_detail'),
    path('photo/<int:pk>/delete/',
         views.StockDeleteView.as_view(),
         name = 'stock_delete'),
]
