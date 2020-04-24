from datetime import date
import csv

# Pega a data de Hoje
dataHoje   = date.today()
# Pega o dia da semana 
diaSemana  = dataHoje.weekday() 
# Formata dias da semana na lista
infoSemana = ['SEGUNDA', 'TERCA', 'QUARTA', 'QUINTA', 'SEXTA', 'SABADO', 'DOMINGO']
# Dia Semana
semana = infoSemana[diaSemana]

infoAulas = []
with open('aulasInfo.csv', encoding='utf-8') as arq:
    csvInfo = csv.reader(arq, delimiter=';')
    for info in csvInfo:
    	infoAulas.append( info )

print('|---------------------------|')
print('|-----| Aulas de Hoje |-----|')
print(f'|-----|  {dataHoje:%d/%m/%Y}   |-----|'  )
print('|---------------------------|')
for i in infoAulas:
	if i[0] == semana:
		print(i)


