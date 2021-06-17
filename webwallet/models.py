from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#teste
class Carteira(models.Model):
    nome = models.CharField(max_length=100)
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)

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
    def getcartatu(iddacarteira, dataini, datafin, intervalo='diario'):
        return json

    def getcarteiras(iddocliente, dataini, datafin, intevalo='diario'):
        return json

    def getdolar(dataini, datafin, intervalo='diario'):
        return json

    def getbtc(dataini, datafin, intervalo='diario'):
        return json

    def getibov(dataini, datafin, intervalo='diario'):
        return json

    def getCotacao(ticker, dataini, datafin, intervalo='diario'):
        start_date=datetime.strptime(dataini, '%Y-%m-%d')
        end_date=datetime.strptime(datafin, '%Y-%m-%d')
        tickers = ticker
        armazena = Acao.objects.filter(ticker_exact = tickers) & Acao.objects.filter (data_cotacao_range= [start_date,end_date])
        a = '{"data":['
        for Acao in armazena:
	        a+= '{"data_cotacao":'+'"'+str(Acao.data_cotacao)+'"'+','
	        a+= '"cotacao":'+str(Acao.cotacao)+'}'+','				
        a = a[0:-1]
        a+= ']}'
        return a

class Cadastro(models.Model):
    
    nome = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False)
    telefone = models.CharField(max_length=15, null=False)
    senha = models.CharField(max_length=100, null=False)
    confirma_senha = models.CharField(max_length=100, null=False)