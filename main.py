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
all_cities = {

}


# Si le div est trouvé, recherchez le span à l'intérieur
for div in weather_bloc:
    span = div.find('span', class_='icon_text')
    a_tag = div.find('a', href=True)
    img_alt = div.find('img', alt=True)
    
    if span:
        temperature = span.text.replace('°', '')
        print("Content of span :", temperature)  # Extract text of span
        
    else:
        print("No span found.")
    if a_tag:
        href = a_tag['href']
        city = href.split('/')[2]
        print(f"City : {city.capitalize()}")
    if img_alt:
        weather_today = img_alt['alt']
        print(f"Weather today: {weather_today}")
    all_cities[city] = {"temperature": temperature, "weather": weather_today}
# else:
#     print("No div found.")

print(all_cities)
map_time_picker = soup.find('div', id='map_time_picker')

if map_time_picker:

    days = map_time_picker.find_all('li')
    first_day = days[0]
    date_today = first_day.find('strong')

    if date_today:
        print(f"Date of the day : {date_today.text}")

    active_element = first_day.find('li', class_='sub_element active')
    if active_element:
        active_time = active_element.find('small')
        print(active_time.text)
# print(f"The weather today is : {weather}")
# Voir le code html source
# print(response.content)