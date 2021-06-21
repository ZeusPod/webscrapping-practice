from bs4 import BeautifulSoup
import requests
import csv

#asiganmos la url que vamos a scrappear 
url = "http://quotes.toscrape.com/"
#hacemos un rquest de la url
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
#extraer los autores de las citas 
quotes_html = soup.find_all('span' , class_="text")
authors_html = soup.find_all('small' , class_="author") 
#crear una lista de las citas
quotes = list()

for quote in quotes_html:
    quotes.append(quote.text)

#crear una lista de las autores 
authors = list()

for author in authors_html:
    authors.append(author.text)

# Para hacer el test: combinar y mostrar las entradas de ambas listas
for t in zip(quotes, authors):
    print(t)
# Guardar las citas y los autores en un archivo CSV en el directorio actual
# Abrir el archivo con Excel / LibreOffice, etc.
with open('./zitate.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file, dialect='excel')
    csv_writer.writerows(zip(quotes, authors))