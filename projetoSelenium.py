import unicodedata
from selenium import webdriver
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

#entrar no site
servico = Service(executable_path=ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

# #2- importar base de dados
tabela = pd.read_excel("commodities.xlsx")
print(tabela)

#Tratando erros de padrão br para padrão americano  
# pra usar na hora de digitar o site

# link = f'https://www.melhorcambio.com/{produto}-hoje'
#     link = unicodedata.normalize("NFKD",link).encode('ascii', 'ignore')
#     link = link.decode('utf-8')
#     navegador.get(link)


# #3- para cada produto da nossa base 
for i in tabela.index:
    produto = tabela.loc[i,"Produto"]
    link = f'https://www.melhorcambio.com/{produto}-hoje'
    link = unicodedata.normalize("NFKD",link).encode('ascii', 'ignore')
    link = link.decode('utf-8')
    navegador.get(link)


    # #4- pegar o preço atual do produto
    cotacao = navegador.find_element('xpath','//*[@id="comercial"]').get_attribute('value')
    cotacao = cotacao.replace('.','').replace(',','.')
    cotacao = float(cotacao)
    tabela.loc[i,'Preço Atual'] = cotacao
    tabela["Comprar"] = tabela["Preço Atual"] < tabela["Preço Ideal"]
print(tabela)
tabela.to_excel("comodities_atualizdo.xlsx", index=False)
navegador.quit()
