from django.core.management.base import BaseCommand
from django.db.models import Max
from yahooquery import Ticker
from webwallet.models import Acao
from datetime import datetime

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        tickers = Acao.objects.distinct().values('ticker')
        ult_data = Acao.objects.aggregate(Max('data_cotacao'))
        for ticker in tickers:
            nome = ticker+'.sa'
            stock = Ticker(nome).price

            if stock[nome]['marketState'] == 'REGULAR' and stock[nome]['regularMartketTime'][0:10] != str(ult_data):
                hoje = stock[nome]['regularMartketTime'][0:10]
                cotacao = stock[nome]['regularMarketPrice']
                acao = Acao(ticker=ticker, data_cotacao=hoje, cotacao=cotacao)
                acao.save()