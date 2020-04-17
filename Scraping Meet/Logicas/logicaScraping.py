from bs4 import BeautifulSoup

arq = open('htmlSite.txt', 'r')
html = arq.read()
arq.close()


page     = BeautifulSoup(html, 'html.parser')
divs     = page.find_all('div', {'class':'z38b6 CnDs7d hPqowe'})
divs     = divs[0]
blocoMsg = divs.find_all('div', {'class':'GDhqjd'})
lastMsg  = len(blocoMsg) - 1

for i in blocoMsg:
	nome = i.find_all('div', {'class':'YTbUzc'})
	msg  = i.find_all('div', {'class':'oIy2qc'})
	
	if nome == []:
		pass
	else:
		print('Nome: ', nome[0].text)

	if msg == []:
		pass
	else:
		for plv in msg:
			print('Mensagem: ', plv.text)

	print('')

input('')