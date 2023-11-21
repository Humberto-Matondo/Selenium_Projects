import requests #modulo para fazer requisicoes para o servidor

url = 'https://astronaut-landing-page.netlify.app'

response = requests.get(url) #Response e a responsta que o servidor vai passar-te. 

print(response.status_code) # para ver o codigo re responta do servidor
#print(response.headers) # para ver o cabecalho do conteudo 
#print(response.contect) # para ver o conteudo que se encontra no servidor em Bytes
#print(response.json()) # usa-se para converter APIs em json para usares.  
print(response.text) # para ver o conteudo que se encontra no servidor em text(HTML completo)
