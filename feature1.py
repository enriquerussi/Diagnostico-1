import json

def cargar_datos(ruta):
    with open(ruta) as contenido:
        json.load(contenido)

if __name__ == '__main__':
    ruta = 'farmers-protest-tweets-2021-03-5.json'
    mas_reteweetts = sorted(cargar_datos(ruta), key=lambda k: k["retweetedTweet"], reverse=True)
    mas_reteweetts = mas_reteweetts[:10]