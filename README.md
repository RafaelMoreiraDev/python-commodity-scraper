#Commodity Price Scraper
é um script Python que automatiza o processo de recuperação e atualização dos preços atuais de várias commodities de um site específico. Ele usa técnicas de web scraping com as bibliotecas Selenium e pandas para coletar os dados e armazená-los em um arquivo do Excel.

##As principais características do Commodity Price Scraper incluem:

Recuperação automatizada de preços de commodities: o script lê uma lista de commodities de um arquivo Excel e navega até um site para coletar os preços atuais de cada commodity.
Manipulação e armazenamento dos dados: Os preços captados são processados 
e armazenados em um arquivo Excel, incluindo informações adicionais como se é o momento ideal para comprar a commodity com base em critérios pré-definidos.
Manipulação de inconsistências de formato de dados: o script cuida da conversão dos preços copiados para um formato padronizado para garantir a manipulação e comparação precisas dos dados.
O script pode ser útil para indivíduos ou empresas interessadas em monitorar e analisar preços de commodities para fins de tomada de decisão, como acompanhar tendências de mercado ou identificar oportunidades de compra favoráveis.
---
##Instalação
Para usar siga as etapas de instalação descritas no arquivo README. Certifique-se de ter o Python 3.11 instalado e instale os pacotes Python. Além disso, você precisará baixar e instalar o driver da web Chrome para Selenium.

##Uso
Para usar o Commodity Price Scraper, siga estas etapas:

Prepare seus dados de commodities: Crie um arquivo Excel chamado "commodities.xlsx" e preencha-o com uma lista de commodities que você deseja rastrear. Certifique-se de incluir uma coluna chamada "Produto" para os nomes das mercadorias.
Execute o script: Execute o comando python scraper.pyem seu terminal ou prompt de comando para iniciar o processo de raspagem.
O script abrirá uma janela do navegador Chrome e navegará para um site específico para obter os preços atuais de cada mercadoria na lista.
Os preços raspados serão processados e salvos em um novo arquivo Excel chamado "commodities_atualizdo.xlsx", que incluirá uma coluna adicional indicando se é o momento ideal para comprar cada commodity com base em critérios pré-definidos.
Sinta-se à vontade para personalizar o código e adaptá-lo às suas necessidades específicas. Se você encontrar algum problema ou tiver alguma sugestão, abra um problema no repositório do GitHub.


