import os
import re
import smtplib
from email.message import EmailMessage
from time import sleep

import openpyxl  # instala-se
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

EDGE_DRIVER_EXEC = 'C:/Users/HP/Desktop/ProjetosPYTHON/Selenium_Projects/drivers/msedgedriver.exe'

class Scrappy: 

    def __init__(self):
        edge_options = Options()
        edge_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        edge_options.add_argument('--lang=pr-BR')
        edge_options.add_argument('--disable-notifications')

        self.driver = webdriver.Edge(executable_path=os.getcwd() + os.sep + 'msedgedriver.exe', options=edge_options)
        
        self.driver.set_window_size_limit(800 ,700)
        self.link = 'https://www.backmarket.com/en-us/l/iphone/e8724fea-197e-4815-85ce-21b8068020cc'

    def iniciar(self):
        self.obter_usuario_e_senha()
        self.raspar_dados_do_site()
        self.criar_panilha_excel()
        self.enviar_email_para_cliente()
        
    def obter_usuario_e_senha(self):

        os.system('clear')
        self.email = input('Informe o email para receber o relatorio dos precos os Iphones.\nEMail: ')
        self.email.lower().strip()
        
        self.senha = input('Senha: ')

        validador_de_email = re.search(r'[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$', self.email)
        if validador_de_email:
            print('EMAIL VALIDO!')
        else: 
            print('Digite um email valido!')
            self.obter_usuario_e_senha()

    def raspar_dados_do_site(self):

        print(self.driver.title)
        self.lista_nome_iphone = []
        self.lista_preco_iphone = []
        self.driver.get(self.link)
        sleep(2)


    def criar_panilha_excel(self):
        ...

    def enviar_email_para_cliente(self):
        ... 

start = Scrappy()
start.iniciar()