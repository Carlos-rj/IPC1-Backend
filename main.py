from flask import Flask, jsonify, request

from flask_cors import CORS
from Persona import Persona

import json

Personas = []
Personas.append(Persona('Carlos','Jimenez',22))
Personas.append(Persona('Roberto','Perez',22))
Personas.append(Persona('Ana','Solorzano',21))
Personas.append(Persona('Pancha','Lopez',23))

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def rutaInicial():
    return("<h1>Hola alumnos</h1>")

@app.route('/', methods=['POST'])
def rutaPost():
    objeto = {"Mensaje":"Se hizo el POST correctamente"}
    return(jsonify(objeto))

@app.route('/Personas', methods=['GET'])
def getPersonas():
    global Personas
    Datos = []
    for persona in Personas:
        objeto = {
            'Nombre': persona.getNombre(),
            'Apellido': persona.getApellido(),
            'Edad': persona.getEdad()
        }
        Datos.append(objeto)
    return(jsonify(Datos))

@app.route('/Personas/<string:nombre>', methods=['GET'])
def ObtenerPersona(nombre): 
    global Personas
    for persona in Personas:
        if persona.getNombre() == nombre:
            objeto = {
            'Nombre': persona.getNombre(),
            'Apellido': persona.getApellido(),
            'Edad': persona.getEdad()
            }
            return(jsonify(objeto))
    salida = { "Mensaje": "No existe el usuario con ese nombre"}
    return(jsonify(salida))

@app.route('/Personas', methods=['POST'])
def AgregarUsuario():
    global Personas
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    edad = request.json['edad']
    nuevo = Persona(nombre,apellido,edad)
    Personas.append(nuevo)
    return jsonify({'Mensaje':'Se agrego el usuario exitosamente',})

@app.route('/Personas/<string:nombre>', methods=['PUT'])
def ActualizarPersona(nombre):
    global Personas
    for i in range(len(Personas)):
        if nombre == Personas[i].getNombre():
            Personas[i].setNombre(request.json['nombre'])
            Personas[i].setApellido(request.json['apellido'])
            Personas[i].setEdad(request.json['edad'])
            return jsonify({'Mensaje':'Se actualizo el dato exitosamente'})
    return jsonify({'Mensaje':'No se encontro el dato para actualizar'})

@app.route('/Personas/<string:nombre>', methods=['DELETE'])
def EliminarPersona(nombre):
    global Personas
    for i in range(len(Personas)):
        if nombre == Personas[i].getNombre():
            del Personas[i]
            return jsonify({'Mensaje':'Se elimino el dato exitosamente'})
    return jsonify({'Mensaje':'No se encontro el dato para eliminar'})
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)