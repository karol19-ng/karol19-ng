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
    retraso = round(columna * 0.04 + fila * 0.01, 2)
    rects.append(f'<rect class="c" style="animation-delay:{retraso}s" x="{x}" y="{y}" width="{TAM}" height="{TAM}" rx="2" fill="{color}"/>')
columnas = columna + 1
ancho = 2 * MARGEN + columnas * PASO
alto = 2 * MARGEN + 7 * PASO + 30

estilo = """<style>
  .c { opacity: 0; transform-box: fill-box; transform-origin: center;
       animation: aparecer 0.4s ease-out forwards; }
  @keyframes aparecer {
    from { opacity: 0; transform: scale(0.4); }
    to   { opacity: 1; transform: scale(1); }
  }
</style>
"""
total=sum(dia["count"] for dia in datos)

y_leyenda = MARGEN + 7 * PASO + 8
extras = []

extras.append(
    f'<text x="{MARGEN}" y="{y_leyenda + 9}" fill="#8b949e" '
    f'font-family="monospace" font-size="10">{total} contribuciones en el último año</text>'
)

x0 = ancho - MARGEN - 30 - 5 * PASO

extras.append(
    f'<text x="{x0 - 4}" y="{y_leyenda + 9}" fill="#8b949e" '
    f'font-family="monospace" font-size="10" text-anchor="end">Menos</text>'
)

for i, color in enumerate(PALETA):
    extras.append(
        f'<rect x="{x0 + i * PASO}" y="{y_leyenda}" width="{TAM}" height="{TAM}" rx="2" fill="{color}"/>'
    )

extras.append(
    f'<text x="{x0 + 5 * PASO + 2}" y="{y_leyenda + 9}" fill="#8b949e" '
    f'font-family="monospace" font-size="10">Más</text>'
)


svg = (
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{ancho}" height="{alto}" viewBox="0 0 {ancho} {alto}">\n'
    + estilo
    + f'<rect width="{ancho}" height="{alto}" fill="#0d1117"/>\n'
    + "\n".join(rects)
    + "\n"
    + "\n".join(extras)
    + "\n</svg>"
)



with open("contrib-heatmap.svg", "w", encoding="utf-8") as archivo:
    archivo.write(svg)
