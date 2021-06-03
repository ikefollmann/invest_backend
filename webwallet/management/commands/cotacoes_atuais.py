from django.core.management.base import BaseCommand
from django.db.models import Max
from yahooquery import Ticker
from webwallet.models import Acao

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        ult_data = Acao.objects.aggregate(Max('data_cotacao'))
        acoes = Acao.objects.filter(data_cotacao=ult_data)
        for acao in acoes:
            ticker = acao.ticker+'.sa'
            stock = Ticker(ticker)
            cotacao = stock.price[ticker]['regularMarketPrice']

            acao.cotacao = float(cotacao)
            acao.save()