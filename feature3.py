import json

def cargar_datos(ruta):
    with open(ruta) as contenido:
        json.load(contenido)

if __name__ == '__main__':
    ruta = 'farmers-protest-tweets-2021-03-5.json'
    date = sorted(cargar_datos(ruta), key=lambda k: k["date"], reverse=True)
    date = date[:10]