from django.urls import path
from subjects import views

urlpatterns = [
    path('', views.subject_list, name='subject_list'),
    path("<int:pk>/", views.subject_detail, name='subject_detail'),
    path('subjects/<int:subject_id>/topics/', views.topic_list, name='topic_list'),
    path('topics/<int:topic_id>/books/', views.book_list, name='book_list'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
    path('chapters/<int:chapter_id>/notes/', views.chapter_notes, name='chapter_notes'),
]