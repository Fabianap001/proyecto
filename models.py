#BLOQUE IMPORT
import os
import json
#BLOQUE APERTURA ARCHIVO JSON
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__)) #-> Detectamos el directorio de este archivo ".py" que contiene este código.
my_file = os.path.join(THIS_FOLDER + '/DB/' 'base_de_datos.json') #-> A ese directorio le sumamos el del archivo. La ruta total se almacena en my_file
#Aquí "os" detecta el directorio donde se ejecuta nuestro archivo python es decir en este caso "models.py" y a partir de allí almacena esta ruta en THIS_FOLDER. Luego ya sabiendo que la ruta es donde está "models.py" bastará agregarle el directorio DB y finalmente indicar el nombre de archivo.
# --> Cargar archivo JSON   
with open (my_file, "r") as f: #->Abrimos pasando como arg la variable my_file que contiene ruta completa Y ALMACENAMOS EN "f"
    datos = json.load(f) #-> Almacenamos en la variable "datos" la interpreteación de nuestro JSON que está almacenado en "f"
#Ahora datos es un diccionario.
#Almacenamos los diccionarios en una sola variable:
datos_personas = datos['Personas']
#Ahora "datos_personas" almacena los diccionarios.
#Así que nos basta con indicar el index y el nombre de CLAVE PARA IMPRIMIR UN VALOR
#print(datos_personas[0]['test'])
#BLOQUE CLASE PERSONA Y CRUD
class Persona(object):
    contador_id = 0 #Creamos una variable contador
    def __init__(self, nombre, apellido, apodo, telefono, direccion):
        self.id = Persona.contador_id #Atriuto id es igual a la variable
        Persona.contador_id +=1 #Sumamos uno al valor actual de la variable
        self.nombre = nombre
        self.apellido = apellido
        self.apodo = apodo
        self.telefono = telefono
        self.direccion = direccion
        #Método CREATE -> Crear una nueva persona o contacto de la base de datos
    def crear_contacto(self):
        #Creamos nueva instancia
            nueva_persona = Persona(
                self.nombre,
                self.apellido,
                self.apodo,
                self.telefono, 
                self.direccion).__dict__ #Guardamos la nueva persona es decir "instancia" dentro de la variable "nueva_persona" como DICCIONARIO
                #Abrimos nuevamente el JSON pero en modo de escritura "w" y con un nuevo nombre de instancia "fr"
            with open (my_file, "w") as fr: #->Estamos abriendo exactamente de la misma forma pero con "w"
                datos['Personas'].append(nueva_persona) #->Entramos a los valores de la clave "Personas" que son Lista y añadimos el nuevo objeto (diccionario)
                json.dump(datos, fr, indent =4) #Finalmente almacenamos en la base de datos argumentando ademas un identado.