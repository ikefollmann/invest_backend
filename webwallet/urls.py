# from django.urls import path
# from . import views

# urlpatterns = [
#     path('index', views.index, name='index'),
#     path('blog', views.blog, name='blog'),
#     path('blog-detalhe', views.blogdetalhe, name='blog-detalhe'),
#     path('ajuda', views.ajuda, name='ajuda'),
#     path('cadastro', views.cadastro, name='cadastro'),
#     path('carteira', views.carteira, name='carteira'),
#     path('conta', views.conta, name='conta'),
#     path('login', views.login, name='login'),
#     path('relatorio', views.relatorio, name='relatorio'),
# ]

from django.conf.urls import url

from . import views

app_name = 'users'
urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^login/$', views.login_view, name="login"),
    url(r'^logout/$', views.logout_view, name="logout"),
    url(r'^register/$', views.RegistrationView.as_view(), name="register"),
]