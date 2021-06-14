from django.core.management.base import BaseCommand
from webwallet.models import Acao
import csv

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        ano = 2021
        if ano > 2001:
            filename = '../../dados/COTAHIST_A'+str(ano)+'.TXT'
        else:
            filename = '../dados/COTAHIST_A'+str(ano)

        with open(filename) as file:
            content = file.read().splitlines()

        for line in content:
            tipo = line[0:2]
            if tipo != '01':
                continue

            codbdi = line[10:12]
            if codbdi not in ['02', '05', '07', '08', '12', '14']:
                continue

            tpmerc = line[24:27]
            if tpmerc not in ['010']:
                continue

            codneg = line[12:24]
            codneg = codneg.strip()
            if codneg[-1] == 'B' or codneg[-2:] in ('34', '12', '35', '39', '33', '32', '13'):
                continue

            preco = line[108:121]
            preco = preco[:-2]+'.'+preco[-2:]
            preco = float(preco)
            data = line[2:6]+'-'+line[6:8]+'-'+line[8:10]

            acao = Acao(cotacao=preco, data_cotacao=data, ticker=codneg)
            acao.save()