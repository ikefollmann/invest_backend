from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from django.contrib.auth.models import User, Group
from webwallet.serializers import UserSerializer, GroupSerializer
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def index(request):
    return render(request = request, template_name = 'front/index.html', context={'form':form})

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

def register(request):
    return render(request = request, template_name = 'registration/register.html')
