from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from django.contrib.auth.models import User, Group
from webwallet.serializers import UserSerializer, GroupSerializer
from django.contrib.auth.forms import UserCreationForm

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
    return render(request = request, template_name = 'relatorio.html')

def conta(request):
    return render(request = request, template_name = 'conta.html')
