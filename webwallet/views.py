from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from django.contrib.auth.models import User, Group
from webwallet.serializers import UserSerializer, GroupSerializer
from django.contrib.auth.forms import UserCreationForm
from webwallet.models import Ativo, Relatorio


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

def index(request):
    return render(request = request, template_name = 'index.html')

def blog(request):
    return render(request = request, template_name = 'blog.html')

def ajuda(request):
    return render(request = request, template_name = 'ajuda.html')

def blogdetalhe(request):
    return render(request = request, template_name = 'blog-detalhe.html')

def cadastro(request):
    return render(request = request, template_name = 'cadastro.html')

def login(request):
    return render(request = request, template_name = 'login.html')

def carteira(request):
    return render(request = request, template_name = 'carteira.html')

def relatorio(request):
    relatorio = Relatorio.getPosAtu(15, '2021-06-27')
    context = {
        "relatorio": relatorio
    }
    return render(request = request, template_name = 'relatorio.html', context = context)

def conta(request):
    return render(request = request, template_name = 'conta.html')


# from django.shortcuts import render
# from django.views.generic import CreateView
# from django.http import HttpResponseRedirect
# from django.contrib.auth.views import login
# from django.contrib.auth.views import logout
# from django.core.urlresolvers import reverse_lazy, reverse

# from .forms import CustomUserCreationForm


# def home(request):
#     return render(request, 'users/home.html')


# def login_view(request, *args, **kwargs):
#     if request.user.is_authenticated():
#         return HttpResponseRedirect(reverse('users:home'))

#     kwargs['extra_context'] = {'next': reverse('users:home')}
#     kwargs['template_name'] = 'users/login.html'
#     return login(request, *args, **kwargs)


# def logout_view(request, *args, **kwargs):
#     kwargs['next_page'] = reverse('users:home')
#     return logout(request, *args, **kwargs)


# class RegistrationView(CreateView):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy('users:login')
#     template_name = "users/register.html"
