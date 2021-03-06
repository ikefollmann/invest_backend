from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from dateutil import rrule
from django.utils.translation import ugettext as _
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db.models import Sum


# Create your models here.
class Cadastro(models.Model):
    nome = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False)
    telefone = models.CharField(max_length=15, null=False)
    senha = models.CharField(max_length=100, null=False)
    confirma_senha = models.CharField(max_length=100, null=False)


class Carteira(models.Model):
    nome = models.CharField(max_length=100)
    cliente = models.ForeignKey(Cadastro, on_delete=models.CASCADE)

    def addativo(self, ticker, datadacompra, precodecompra):
        ativo = Ativos(ticker, datadacompra, precodecompra)
        return 0

    def delativo(self, iddoativo):
        ativo = Ativos.Delete(iddoativo)
        return 0

    def getrelcartatu(self, dataini, datafin):
        idcarteira = self.id
        json = Relatorios.getcartatu(iddacarteira, dataini, datafin)
        return json

    def getrelcarteiras(self, iddocliente, dataini, datafin):
        json = Relatorios.getcarteiras(idocliente, dataini, datafin)
        return json


class Acao(models.Model):
    cotacao = models.DecimalField(max_digits=12, decimal_places=2)
    data_cotacao = models.DateField(db_index=True)
    ticker = models.CharField(max_length=10, db_index=True)


class Ativo(models.Model):
    ticker = models.CharField(max_length=10, db_index=True)
    data_compra = models.DateField()
    preco_compra = models.DecimalField(max_digits=12, decimal_places=2)
    carteira = models.ForeignKey(Carteira, on_delete=models.CASCADE, db_index=True)
    cotas = models.PositiveBigIntegerField(default=1)
    

class Relatorio(models.Model):
    def getPosAtu(iddacarteira, dataatu):
        ativos = Ativo.objects.filter(carteira=iddacarteira, data_compra__lte=dataatu)
        dados = []
        for ativo in ativos:
            aux = []
            ticker = []
            posicao = []

            cotacao = Acao.objects.filter(ticker=ativo.ticker, data_cotacao__lte=dataatu).latest('data_cotacao').cotacao
            valor = cotacao * ativo.cotas

            ticker.append(ativo.ticker)
            posicao.append(valor)

            aux.append(ticker)
            aux.append(posicao)

            dados.append(aux)

        return dados


    def getcartatu(iddacarteira, dataini, datafin, intervalo='diario'):
        datas = []
        if intervalo == 'mensal':
            for date in rrule.rrule(rrule.MONTHLY, dtstart=datetime.strptime(dataini, '%Y-%m-%d'), until=datetime.strptime(datafin, '%Y-%m-%d')):
                datas.append(date)
        else:
            for date in rrule.rrule(rrule.DAILY, dtstart=datetime.strptime(dataini, '%Y-%m-%d'), until=datetime.strptime(datafin, '%Y-%m-%d')):
                datas.append(date)
        json = '{"data": ['
        for date in datas:
            ativos = Ativo.objects.filter(carteira=iddacarteira, data_compra__lte=date.date())
            posicao = 0
            for ativo in ativos:
                posicao += Acao.objects.filter(ticker=ativo.ticker, data_cotacao__lte=date.date()).latest('data_cotacao').cotacao * ativo.cotas
            json += '{"dia": "'+str(date.date())+'", "posicao": '+str(posicao)+'},'
        json = json[:-1]
        json += ']}'            

        return json

    def getcarteiras(iddocliente, dataini, datafin):
        carteiras = Carteira.objects.filter(cliente=iddocliente)
        json = '{"data":['
        for carteira in carteiras:
            ativos = Ativo.objects.filter(carteira=carteira.id)
            ativos_ini = ativos.filter(data_compra__lte=dataini)
            soma_ini = 0
            for ativo in ativos_ini:
                soma_ini += Acao.objects.filter(ticker=ativo.ticker, data_cotacao__lte=dataini).latest('data_cotacao').cotacao * ativo.cotas
            ativos_fin = ativos.filter(data_compra__lte=datafin)
            soma_fin = 0
            for ativo in ativos_fin:
                soma_fin += Acao.objects.filter(ticker=ativo.ticker, data_cotacao__lte=datafin).latest('data_cotacao').cotacao * ativo.cotas
            json += '{"nome": "'+carteira.nome+'", "pos_ini": '+str(soma_ini)+', "pos_fin": '+str(soma_fin)+'},'
        json = json[:-1]
        json += ']}'

        return json

    def getdolar(dataini, datafin, intervalo='diario'):
        pass

    def getbtc(dataini, datafin, intervalo='diario'):
        pass

    def getibov(dataini, datafin, intervalo='diario'):
        pass

    def getCotacao(ticker, dataini, datafin, intervalo='diario'):
        start_date=datetime.strptime(dataini, '%Y-%m-%d')
        end_date=datetime.strptime(datafin, '%Y-%m-%d')
        acoes = Acao.objects.filter(ticker=ticker, data_cotacao__range=[start_date, end_date])
        json = '{"data":['
        for acao in acoes:
	        json += '{"data_cotacao":'+'"'+str(Acao.data_cotacao)+'"'+','
	        json += '"cotacao":'+str(Acao.cotacao)+'}'+','				
        json = json[0:-1]
        json += ']}'
        return json

#gerenciador do usuario, responsavel por salvar
# class Cadastro(BaseUserManager):

#     use_in_migrations = True

#     def _create_user(self, email, password, **extra_fields):
#         if not email:
#             raise ValueError('O e-mail ?? obrigat??rio')
#         email = self.normalize_email(email)
#         user = self.model(email=email, username=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_user(self, email, password=None, **extra_fields):
#         # extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', False)
#         return self._create_user(email, password, **extra_fields)

#     def create_superuser(self, email, password, **extra_fields):
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('is_staff', True)

#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser precisa ter is_superuser=True')

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser precisa ter is_staff=True')

#         return self._create_user(email, password, **extra_fields)


# class CustomUsuario(AbstractUser):
#     email = models.EmailField('E-mail', unique=True)
#     fone = models.CharField('Telefone', max_length=15)
#     is_staff = models.BooleanField('Membro da equipe', default=True)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['first_name', 'last_name', 'fone']

#     def __str__(self):
#         return self.email

#     objects = UsuarioManager()