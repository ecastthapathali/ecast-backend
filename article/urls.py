from django.urls import path, include
from .views import ArticleListCreate, ArticleDetail

urlpatterns = [
    path('form/', ArticleListCreate.as_view(), name='article-list-create'),
    path('form/<int:pk>/', ArticleDetail.as_view(), name='article-detail'),
]