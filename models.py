#BLOQUE IMPORT
import os
import json

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

my_file = os.path.join(THIS_FOLDER + '/DB/' 'base_de_datos.json')

#BLOQUE CONEXIÓN CON BASE DE DATOS JSON
with open (my_file, "r") as f: #->Abrimos pasando como arg la variable my_file que contiene ruta completa
    datos = json.load(f)

print(datos['Personas'])

datos_personas = datos['Personas']
#Ahora "datos_personas" almacena los diccionarios.
#Así que nos basta con indicar el index de la lista correspondiente y el nombre de CLAVE PARA IMPRIMIR UN VALOR
print(datos_personas[0]['test'])

class Persona(object):
    contador_id = 0
    def __init__(self, nombre, apellido, apodo, telefono, direccion):
        self.id = Persona.contador_id 
        Persona.contador_id +=1
        self.nombre = nombre
        self.apellido = apellido
        self.apodo = apodo
        self.telefono = telefono
        self.direccion = direccion

#Método CREATE -> Crear una nueva persona o contacto de la base de datos
    def crear_contacto():
        pass
    
    #Método READ -> Leer una persona o contacto de la base de datos
    def leer_contacto():
        pass
    #Método UPDATE -> Actualizar o modificar un dato de algún contacto en la bd
    def actualizar_contacto():
        pass
    #Método DELETE -> Borrar una persona o contacto de la base de datos
    def eliminar_contacto():
        pass
#persona_test = Persona(0, "Mariano", "Laca", "Pyromaniac", "34343434", "pythones.net").__dict__
#print(persona_test)
    
persona_test = Persona("Mariano", "Laca", "Pyromaniac", "34343434", "pythones.net").__dict__
persona_test2 = Persona("Mariano", "Laca", "Pyromaniac", "34343434", "pythones.net").__dict__
print(persona_test)
print(persona_test2)
persona_test3 = Persona("Mariano", "Laca", "Pyromaniac", "34343434", "pythones.net").__dict__
print(persona_test3)

