"""
    AUTOMAÇÃO PARA O MEU PERFIL DO LINKDIN.
"""

from pathlib import Path
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys #todas as teclas se encontram aqui, Ex: enter, space e etc...
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait  

ROOT_FOLDER = Path(__file__).parent
EDGE_DRIVER_EXEC = ROOT_FOLDER / 'drivers' / 'msedgedriver.exe'

def make_edge_browser(*options: str) -> webdriver.Edge:

    edge_options = webdriver.EdgeOptions()

    if options is not None:
        for option in options:
            edge_options.add_argument(option)  # type: ignore

    edge_service = Service(
        executable_path=str(EDGE_DRIVER_EXEC),
    )

    browser = webdriver.Edge(
        service=edge_service,
        options=edge_options
    )

    return browser


if __name__ == '__main__':
    TIME_TO_WAIT = 5
    options = ()
    browser = make_edge_browser(*options)

    browser.get('https://www.google.com')

    #espere para encontrar o <textarea> na barra de pesq. do google:
    barra_pesquisa = WebDriverWait(browser, TIME_TO_WAIT).until(
        EC.presence_of_element_located(
            (By.ID, 'APjFqb')
        )
    ) 

    barra_pesquisa.send_keys('Quem é Humberto Matondo?')
    barra_pesquisa.send_keys(Keys.ENTER) # para dar o enter e pesquisar. 

    result = browser.find_element(By.ID,'search') # encontrou e selecionou os elementos
    links = result.find_elements(By.TAG_NAME,'a') # vai ficar o elemento desejado
    #print(links[0]) # para ver o primeiro link
    links[0].click() #para clicar no primeiro link da pagina. 
    
    sleep(TIME_TO_WAIT)
