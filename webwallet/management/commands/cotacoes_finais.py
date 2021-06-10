from django.core.management.base import BaseCommand
from django.db.models import Max
from yahooquery import Ticker
from webwallet.models import Acao
from datetime import date

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        hoje = date.today()
        ult_data = Acao.objects.aggregate(Max('data_cotacao'))

        if hoje == ult_data:
            acoes = Acao.objects.filter(data_cotacao=ult_data)
            for acao in acoes:
                ticker = acao.ticker+'.sa'
                stock = Ticker(ticker).price

                if stock[ticker]['marketState'] == 'POSTPOST':
                    cotacao = stock[ticker]['regularMarketPrice']
                    acao.cotacao = float(cotacao)
                    acao.save()