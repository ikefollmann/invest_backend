from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from django.contrib.auth.models import User, Group
from webwallet.serializers import UserSerializer, GroupSerializer
from django.contrib.auth.forms import UserCreationForm
from .application import importa_dados, importa_btc

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
    return HttpResponse("Hello World!!!")

def register(request):
    form = UserCreationForm
    return render(request = request, template_name = 'registration/register.html', context={'form':form})

def teste(request):
    importa_dados.importa(2021)
    #print('testando')
    return HttpResponse("Será que deu insert?")

def dadosbtc(request):
    teste = importa_btc.importa()
    return HttpResponde(teste)
