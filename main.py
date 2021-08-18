import json

def cargar_datos(ruta):
    with open(ruta) as contenido: 
        resultado =json.load(contenido)
        print(resultado)



if __name__ == '__main__': 
    ruta = 'json/leer.json'
    cargar_datos(ruta)
