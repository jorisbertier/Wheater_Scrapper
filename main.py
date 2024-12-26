import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time


driver = webdriver.Chrome()  # Or webdriver.Firefox() navegator

url = "https://meteofrance.com/"
driver.get(url)

# Attendez quelques secondes pour que le JavaScript charge le contenu
time.sleep(5)

# Récupérez le contenu HTML rendu par le navigateur
html = driver.page_source

# Analysez le HTML avec BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Recherchez le div avec la classe spécifiée
weather_bloc = soup.find_all('div', class_='leaflet-marker-icon')

# Si le div est trouvé, recherchez le span à l'intérieur
for div in weather_bloc:
    span = div.find('span', class_='icon_text')
    a_tag = div.find('a', href=True)
    img_alt = div.find('img', alt=True)
    
    if span:
        print("Contenu du span :", span.text)  # Extraction du texte du span
    else:
        print("Aucun span trouvé.")
    if a_tag:
        href = a_tag['href']
        location = href.split('/')[2]
        print(location.capitalize())
    if img_alt:
        print(img_alt['alt'])
else:
    print("Aucun div trouvé.")

# map_time_picker = soup.find('div', id='map_time_picker')
# print(map_time_picker)
# if map_time_picker:
#     days = map_time_picker.find_all('li')

#     for day in days:
#         date = day.find('strong')
#         if date:
#             print(f"Date : {date.text}")
# print(f"The weather today is : {weather}")
# Voir le code html source
# print(response.content)