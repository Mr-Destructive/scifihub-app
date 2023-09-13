from django.urls import path

from book import views

app_name = 'books'

urlpatterns = [
    path('', views.book_list, name='list'),
    path('<slug:slug>/', views.book_detail, name='detail'),
]
