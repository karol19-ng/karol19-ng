from html import escape

# Filas de contenido: (etiqueta, valor)
FILAS = [
    ("Rol", "Programadora junior y analista junior de ciberseguridad"),
    ("Ahora", "Buscando trabajo"),
    ("Stack", "Python, C, Java, JavaScript, HTML, CSS, .NET, Docker, Git, Hangfire"),
    ("Datos", "MySQL, PostgreSQL, MongoDB, SQLite, SQL Server, Firebase"),
    ("Herramientas", "VS Code, Google Cloud, NetBeans, Postman, DBeaver, GitHub"),
    ("Foco", "Desarrollo web y de software, ciberseguridad, bases de datos, IA"),
]

TITULO = "karol19-ng@github"

ANCHO = 720
MARGEN = 20
ALTO_LINEA = 24
X_VALOR = MARGEN + 130
VERDE = "#39d353"
GRIS = "#c9d1d9"
FONDO = "#0d1117"
BORDE = "#30363d"

alto = 2 * MARGEN + (len(FILAS) + 2) * ALTO_LINEA

lineas = []

# Título
lineas.append(
    f'<text x="{MARGEN}" y="{MARGEN + ALTO_LINEA}" fill="{VERDE}" '
    f'font-family="monospace" font-size="16" font-weight="bold">{escape(TITULO)}</text>'
)

# Línea separadora debajo del título
y_linea = MARGEN + ALTO_LINEA + 10
lineas.append(
    f'<line x1="{MARGEN}" y1="{y_linea}" x2="{ANCHO - MARGEN}" y2="{y_linea}" '
    f'stroke="{BORDE}" stroke-width="1"/>'
)

# Filas: etiqueta en verde, valor en gris
for i, (etiqueta, valor) in enumerate(FILAS):
    y = MARGEN + (i + 2) * ALTO_LINEA + 10
    lineas.append(
        f'<text x="{MARGEN}" y="{y}" fill="{VERDE}" '
        f'font-family="monospace" font-size="13">{escape(etiqueta)}</text>'
    )
    lineas.append(
        f'<text x="{X_VALOR}" y="{y}" fill="{GRIS}" '
        f'font-family="monospace" font-size="13">{escape(valor)}</text>'
    )

svg = (
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{ANCHO}" height="{alto}" viewBox="0 0 {ANCHO} {alto}">\n'
    f'<rect width="{ANCHO}" height="{alto}" rx="10" fill="{FONDO}" stroke="{BORDE}"/>\n'
    + "\n".join(lineas)
    + "\n</svg>"
)

with open("info-card.svg", "w", encoding="utf-8") as archivo:
    archivo.write(svg)