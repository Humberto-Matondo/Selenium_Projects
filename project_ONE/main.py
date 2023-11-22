from pathlib import Path
from time import sleep

from selenium import webdriver
from selenium.webdriver.edge.service import Service

ROOT_FOLDER = Path(__file__).parent
EDGE_DRIVER_EXEC = ROOT_FOLDER / 'drivers' / 'msedgedriver.exe'

def make_edge_browser(*options: str) -> webdriver.Edge:

    edge_options = webdriver.EdgeOptions()

    # edge_options.add_argument('--headless')
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
    # Example
    # options =( '--headless', '--disable-gpu', ) #forma de usar as os comandos existentes no chrome option 
    # '--headless' -> para fazer tudo por de tras dos panos, ou seja sem abrir o navegador.
    # '--disable-gpu' -> para evitar problemas com a GPU caso estejas a usar uma maquina virtual
    
    options = ()
    browser = make_edge_browser(*options)

    # Como antes
    browser.get('https://www.google.com')
    sleep(5)
