from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup

from senha import *
from time import sleep, strftime

# Lembrando que seu email Google, tem que liberar os Apps menos Seguros nele !
mail_address = 'seu email'
password     = 'seu senha'

drivePath = './chromedriver'
driver = webdriver.Chrome()
urlGoogle = 'https://www.google.com/accounts/' # URL DO LOGIN DO GOOGLE
urlMeet = 'https://meet.google.com/icw-byna-rpp?authuser=2' # URL do CHAT DO MEET

# Autenticar no Google para poder entrar no Meet 
driver.get(urlGoogle)

print('Logando no Google')
driver.find_element_by_id("identifierId").send_keys(mail_address)
driver.find_element_by_xpath('//*[@id="identifierNext"]/span/span').click()
driver.implicitly_wait(10)
driver.find_element_by_name("password").send_keys(password)
driver.find_element_by_xpath('//*[@id="passwordNext"]/span/span').click()
driver.implicitly_wait(5)
sleep(5)

# Abre o Meet em Nova Aba - Agaruda proxima Instrução
print('Abrindo nova Aba do Meet')
driver.execute_script(f"window.open('{urlMeet}', '_blank')")
driver.switch_to_window(driver.window_handles[1])
driver.implicitly_wait(3)
sleep(5)

# Espera o site carregar e clica em participar - Aguarda entrar no chat
print('Clicando em Participar')
driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[3]/div[3]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/div[1]/span/span').click()
driver.implicitly_wait(5)
sleep(5)

# # Clica no botao do chat - Aguarda mais intruções
# print('Clicando no Chat')
# driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[3]/div[3]/div[6]/div[2]/div[3]/span/span').click()

print('\n')

# driver.implicitly_wait(2)
# sleep(2)

# Começa analisar o chat do MEET
print('### Analisando o Chat ##')

echo = False
lastMsg     = ''

comandos = ['/help', '/echo 1', '/echo 0', '/info']
adms = ['Você', 'Matheus Ribeiro', 'Matheus Oliveira']


while True:
	driver.implicitly_wait(1)
	sleep(0.5)

	html        = driver.page_source
	page        = BeautifulSoup(html, 'html.parser')
	divs        = page.find_all('div', {'class':'z38b6 CnDs7d hPqowe'})
	if len(divs) > 0:
		divs        = divs[0]
		blocoMsg    = divs.find_all('div', {'class':'GDhqjd'})
		tamLastMsg  = len(blocoMsg) - 1
		

		if len(blocoMsg) > 0:
			nome = blocoMsg[tamLastMsg].find_all('div', {'class':'YTbUzc'})
			msg  = blocoMsg[tamLastMsg].find_all('div', {'class':'oIy2qc'})

			if nome == []:
				pass
			else:
				attName = nome[0].text
			if msg == []:
				pass
			else:
				attMsg = msg[len(msg)-1].text
				# for plv in msg:
				# 	print('Mensagem: ', plv.text)

			if attName in adms:
				if attMsg in comandos:
					if attMsg == '/echo 1':
						echo = True

					if attMsg == '/echo 0':
						echo = False

					if attMsg == '/info':
						msg1 = 'BoT Criado por Matheus Oliveira'
						msg2 = 'Intuito de Estudo'
						driver.find_element_by_name('chatTextInput').send_keys(f'{msg1}')
						driver.find_element_by_name('chatTextInput').send_keys(Keys.ENTER)
						driver.find_element_by_name('chatTextInput').send_keys(f'{msg2}')
						driver.find_element_by_name('chatTextInput').send_keys(Keys.ENTER)

					if attMsg == '/help':
						driver.find_element_by_name('chatTextInput').send_keys('Lista de Comandos:')
						driver.find_element_by_name('chatTextInput').send_keys(Keys.ENTER)
						driver.find_element_by_name('chatTextInput').send_keys('/help - Mostra os Comandos')
						driver.find_element_by_name('chatTextInput').send_keys(Keys.ENTER)
						driver.find_element_by_name('chatTextInput').send_keys('/info - Informações Sobre o Bot')
						driver.find_element_by_name('chatTextInput').send_keys(Keys.ENTER)
						driver.find_element_by_name('chatTextInput').send_keys('/echo 1 - Ativa o modo Echo')
						driver.find_element_by_name('chatTextInput').send_keys(Keys.ENTER)
						driver.find_element_by_name('chatTextInput').send_keys('/echo 0 - Desativa o modo Echo')
						driver.find_element_by_name('chatTextInput').send_keys(Keys.ENTER)

			if echo == True:
				if lastMsg != attMsg and attName in adms and lastMsg not in comandos:
					lastMsg = attMsg # atualiza a ultima mensagem
					driver.find_element_by_name('chatTextInput').send_keys(f'{lastMsg}')
					driver.find_element_by_name('chatTextInput').send_keys(Keys.ENTER)


	
		




# while True:
# 	teste = int(input('Informe sua ação: '))

# 	if teste == 1:
# 		texto = str(input('Informe o texto: '))
# 		driver.find_element_by_name('chatTextInput').send_keys(f'{texto}')
# 		driver.find_element_by_name('chatTextInput').send_keys(Keys.ENTER)

# 	if teste == 0:
# 		break

# print('Saiu do While')


