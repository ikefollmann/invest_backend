from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('blog', views.blog, name='blog'),
    path('blog-detalhe', views.blogdetalhe, name='blog-detalhe'),
    path('ajuda', views.ajuda, name='ajuda'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('carteira', views.carteira, name='carteira'),
    path('conta', views.conta, name='conta'),
    path('login', views.login, name='login'),
    path('relatorio', views.relatorio, name='relatorio'),
]
