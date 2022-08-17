import json

def cargar_datos(ruta):
    with open(ruta) as contenido:
        json.load(contenido)

if __name__ == '__main__':
    ruta = 'farmers-protest-tweets-2021-03-5.json'
    usuarios = sorted(cargar_datos(ruta), key=lambda k: k["username"], reverse=True)
    usuarios = usuarios[:10]