from flask import Flask, render_template
import os
from random import choice

app = Flask(__name__)

pokeneas = [
    {"id": 1, "nombre": "Pikachu", "altura": 0.4, "habilidad": "Electricidad", "imagen": "https://storage.googleapis.com/pokenea-1/pikashu.png", "frase_filosofica": "A pesar de todo sigo de pie"},
    {"id": 2, "nombre": "Bulbasaur", "altura": 0.7, "habilidad": "Hierba", "imagen": "https://storage.googleapis.com/pokenea-1/bulbasaurio.png", "frase_filosofica": "whigga"},
    {"id": 3, "nombre": "Charmander", "altura": 0.6, "habilidad": "Fuego", "imagen": "https://storage.googleapis.com/pokenea-1/cristinini.png", "frase_filosofica": "ya no mas morbojoooooooooon"},
    {"id": 4, "nombre": "Squirtle", "altura": 0.5, "habilidad": "Agua", "imagen": "https://storage.googleapis.com/pokenea-1/cojone.png", "frase_filosofica": "hola"},
    {"id": 5, "nombre": "Jigglypuff", "altura": 0.5, "habilidad": "Canto", "imagen": "https://storage.googleapis.com/pokenea-1/jiggly.png", "frase_filosofica": "peruan depresion"},
    {"id": 6, "nombre": "Eevee", "altura": 0.3, "habilidad": "Evolución", "imagen": "https://storage.googleapis.com/pokenea-1/perro.png", "frase_filosofica": "yo kreo que los fans de messi y cristiano deberiamos dejar de compararlos y besarnos entre todos"},
    {"id": 7, "nombre": "Snorlax", "altura": 2.1, "habilidad": "Dormir", "imagen": "https://storage.googleapis.com/pokenea-1/drome.png", "frase_filosofica": "hola"}
]


@app.route('/')
def home():
    return "Taller hdp"

@app.route('/json')
def json ():
    container_id = os.getenv('HOSTNAME', 'unknown')
    pokenea = choice(pokeneas)
    data = f"ID: {pokenea['id']}, Nombre: {pokenea['nombre']}, Altura: {pokenea['altura']}, Habilidad: {pokenea['habilidad']}, ID Contenedor: {container_id}"
    return data

@app.route('/foto')
def foto():
    pokenea = choice(pokeneas)
    container_id = os.getenv('HOSTNAME', 'unknown')
    return render_template ('foto.html', imagen=pokenea['imagen'], frase_filosofica=pokenea['frase_filosofica'], container_id=container_id)



if __name__ == '__main__':
    app.run(debug=True)