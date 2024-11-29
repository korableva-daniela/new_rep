
from django.urls import path
from . import views
import os

urlpatterns = [
    path('author/<int:id>/',views.author_info),
    path('author/list',views.author_list),
    path('',views.author_list),
    path('author/add',views.author_create),
    path('author/<int:id1>/update',views.author_update),

    path('book/<int:id>/', views.book_info),
    path('book/list', views.book_list),
    path('book', views.book_list),
    path('book/add', views.book_create),
    path('book/<int:id1>/update', views.book_update)
]


