from django.core.management.base import BaseCommand
from django.db.models import Max
from yahooquery import Ticker
from webwallet.models import Acao
from datetime import datetime

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        tickers = Acao.objects.distinct().values('ticker')
        hoje = datetime.today().date()
        try:
            if Ticker('wege3.sa').price['wege3.sa']['marketState'] == 'REGULAR':
                for ticker_dict in tickers:
                    ticker = ticker_dict['ticker']
                    nome = ticker+'.sa'
                    stock = Ticker(nome).price[nome]
                    try:
                        if stock['regularMarketChangePercent'] != 0:
                            acao = Acao.objects.filter(ticker=ticker).latest('data_cotacao')
                            if acao.data_cotacao == hoje:
                                acao.cotacao = stock['regularMarketPrice']
                                acao.save()
                            else:
                                nova_acao = Acao(ticker=ticker, cotacao=stock['regularMarketPrice'], data_cotacao=hoje)
                                nova_acao.save()
                    except KeyError:
                        file = open('/var/log/django_logs/database_logs.log', 'a')
                        file.write(str(datetime.now()+': Inside Exception: KeyError:'+KeyError+'. Ticker: '+ticker+'\n'))
            else:
                file = open('/var/log/django_logs/database_logs.log', 'a')
                file.write(str(datetime.now()+': Mercado Fechado\n'))
        except KeyError:
            file = open('/var/log/django_logs/database_logs.log', 'a')
            file.write(str(datetime.now()+': Outside Exception: KeyError:'+KeyError+' \n'))
