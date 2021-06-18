from django.core.management.base import BaseCommand
from django.db.models import Max
from yahooquery import Ticker
from webwallet.models import Acao
from datetime import datetime

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        contador = 1
        tickers = Acao.objects.distinct().values('ticker')
        hoje = datetime.today().date()
        try:
            if Ticker('wege3.sa').price['wege3.sa']['marketState'] == 'POSTPOST':
                for ticker_dict in tickers:
                    contador += 1
                    ticker = ticker_dict['ticker']
                    nome = ticker+'.sa'
                    stock = Ticker(nome).price[nome]
                    print(ticker)
                    try:
                        if isinstance(stock, dict):
                            if stock['regularMarketChangePercent'] != 0:
                                acao = Acao.objects.filter(ticker=ticker, data_cotacao=hoje)
                                if acao:
                                    acao[0].cotacao = stock['regularMarketPrice']
                                    acao[0].save()
                                    print('Else: '+str(contador)+'  Acao.ID: '+str(acao[0].id))
                                else:
                                    nova_acao = Acao(ticker=ticker, data_cotacao=hoje, cotacao=stock['regularMarketPrice'])
                                    nova_acao.save()
                                    print('Else: '+str(contador)+'  Nova_Acao.ID: '+str(nova_acao.id))
                    except KeyError:
                        file = open('/var/log/django_logs/database_logs/closed_market.log', 'a')
                        file.write(str(datetime.now()+': Inside Exception: KeyError:'+KeyError+'. Ticker: '+ticker+'\n'))
            else:
                file = open('/var/log/django_logs/database_logs/closed_market.log', 'a')
                file.write(str(datetime.now()+': Mercado Aberto\n'))
        except KeyError:
            file = open('/var/log/django_logs/database_logs/closed_market.log', 'a')
            file.write(str(datetime.now()+': Outside Exception: KeyError:'+KeyError+' \n'))
