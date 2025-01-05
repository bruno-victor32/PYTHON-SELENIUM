from playwright.sync_api import sync_playwright
import time

#com sync_playwright() as p:
with sync_playwright() as p: #Está rodando sync_playwright() e armazenando a resposta do playwright na letra p
    navegador = p.chromium.launch(headless=False) #Criando o navegado do chrome ou do opera ou do edge
    #navegador = p.webkit.launch() #Criando o navegado do safari
    #navegador = p.firefox.launch() #Criando o navegado do firefox

    pagina = navegador.new_page() #Criando uma nova página em branco
    pagina.goto("https://www.hashtagtreinamentos.com/curso-python")
    pagina.locator('xpath=//*[@id="firstname"]').click()
    pagina.fill('xpath=//*[@id="firstname"]',"Bruno")
    time.sleep(2)

    pagina.fill('xpath=//*[@id="email"]', 'bruno.victor32@yahoo.com.br')
    time.sleep(2)

    pagina.fill('xpath=//*[@id="phone"]', '13988615655')
    time.sleep(2)
    #pagina.locator('xpath=//*[@id="_form_2475_submit"]').hover() #Para colocar o mouse em cima do botão
    pagina.locator('xpath=//*[@id="_form_2475_submit"]').click()
    time.sleep(5)