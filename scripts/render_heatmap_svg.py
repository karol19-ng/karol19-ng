import json
from datetime import date

PALETA = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"]
TAM = 11 # lado de cada cuadrado 
PASO = 14 # distancia entre cuadros
MARGEN =10 #borde alrededor del mapa 


with open("data/contributions.json","r",encoding="utf-8") as f:
    data=json.load(f)
    
datos=data["days"]

primera_fecha=date.fromisoformat(datos[0]["date"])
fila_inicio=(primera_fecha.weekday()+1)%7

rects=[]

for n, dia  in enumerate(datos):
    posicion=n+fila_inicio
    columna=posicion//7
    fila=posicion%7
    
    x=MARGEN+columna*PASO
    y=MARGEN+fila*PASO
    color=PALETA[dia["level"]]
    rects.append(f'<rect x="{x}" y="{y}" width="{TAM}" height="{TAM}" rx="2" fill="{color}"/>')

columnas = columna + 1
ancho = 2 * MARGEN + columnas * PASO
alto = 2 * MARGEN + 7 * PASO
svg = (
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{ancho}" height="{alto}" viewBox="0 0 {ancho} {alto}">\n'
    f'<rect width="{ancho}" height="{alto}" fill="#0d1117"/>\n'
    + "\n".join(rects)
    + "\n</svg>"
)

with open("contrib-heatmap.svg", "w", encoding="utf-8") as archivo:
    archivo.write(svg)
