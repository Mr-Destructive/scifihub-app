from django.urls import path

from . import views

app_name = 'books'

urlpatterns = [
    path('', views.book_list, name='list'),
    path('create/', views.book_create, name='create'),
    path('<slug:slug>/', views.book_detail, name='detail'),
    path('edit/<slug:slug>/', views.book_edit, name='edit'),
    path('delete/<slug:slug>/', views.book_delete, name='delete'),
    path('b/<slug:slug>/create/chapter/', views.add_chapter, name='create-chapter'),
    path('b/<slug:book_slug>/chapter/<slug:chp_slug>/', views.chapter_detail, name='chapter-detail'),
]
