from bs4 import BeautifulSoup
from selenium import webdriver
import time
import matplotlib.pyplot as plt


driver = webdriver.Chrome()  # Or webdriver.Firefox() of navigator

url = "https://meteofrance.com/"
driver.get(url)

# Wait a few seconds for the JavaScript to load the content
time.sleep(5)

# Retrieve the HTML content rendered by the browserr
html = driver.page_source

# Parse HTML with BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find the div with the specified class
weather_bloc = soup.find_all('div', class_='leaflet-marker-icon')
all_cities = {}

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
    if city and temperature and weather_today:
        if city not in all_cities: 
            all_cities[city] = {"temperature": temperature, "weather": weather_today}
            print(f"Added {city} with temperature {temperature}°C and weather {weather_today}.")
        else:
            print(f"{city} already exists in the list, updating data.")
            all_cities[city].update({"temperature": temperature, "weather": weather_today})
    else:
        print(f"Data incomplete for {city}. Skipping.")
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
# print(response.content)

cities = list(all_cities.keys())
temperatures = [int(city_data['temperature']) for city_data in all_cities.values()]

max_temp = int(max(temperatures))
min_temp = int(min(temperatures))

plt.bar(height=temperatures, x=cities, label="Température (°C)", color="skyblue", width=0.6)

plt.title("Temperature by cities")
plt.xlabel("All cities France")
plt.ylabel("Temperature (°C)")

plt.ylim(min_temp, max_temp + 2)
# plt.yticks(range(0, max_temp + 3, 2))
plt.xticks(rotation=90)

plt.legend(loc="upper right") 

plt.show()