import requests
from bs4 import BeautifulSoup
import json
import re 

USERNAME = "karol19-ng"
url = f"https://github.com/users/{USERNAME}/contributions"

respuesta = requests.get(url, timeout=10)
respuesta.raise_for_status() #Lanzar un error si la respuesta no es 200
print(respuesta.text.count("data-date")) #Contar las veces que sale la fecha  de cada casilla del calendario de contribuciones




soup = BeautifulSoup(respuesta.text, "html.parser")
celdas = soup.find_all("td", attrs={"data-date": True}) # Buscar todas las celdas con atributo data-date

dias = []
tooltips={}

for tip in soup.find_all("tool-tip"):
    tooltips[tip["for"]] = tip.get_text(strip=True)
    
print(len(tooltips))
    
for celda in celdas:
    
    texto=tooltips.get(celda["id"], "")
    coincidencia = re.match(r"(\d+)",texto)
    conteo =int(coincidencia.group(1)) if coincidencia else 0
    
    dias.append({
        "date": celda["data-date"],
        "level": int(celda["data-level"]),
        "count": conteo,
    })
    
dias.sort(key=lambda dia:dia ["date"])

print(len(dias))
print(dias[:3])

with open("data/contributions.json","w", encoding="utf-8") as archivo:
    json.dump({"username": USERNAME, "days": dias}, archivo, indent=2)