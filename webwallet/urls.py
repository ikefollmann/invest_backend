from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('blog', views.blog, name='blog'),
    path('blog-detalhe', views.blogdetalhe, name='blog-detalhe'),
    path('ajuda', views.blogdetalhe, name='ajuda'),
    path('cadastro', views.blogdetalhe, name='cadastro'),
    path('carteira', views.blogdetalhe, name='carteira'),
    path('conta', views.blogdetalhe, name='conta'),
    path('login', views.blogdetalhe, name='login'),
    path('relatorio', views.blogdetalhe, name='relatorio'),
]
