# #BLOQUE IMPORT
# import os
# import json
# #BLOQUE APERTURA ARCHIVO JSON
# THIS_FOLDER = os.path.dirname(os.path.abspath(__file__)) #-> Detectamos el directorio de este archivo ".py" que contiene este código.
# my_file = os.path.join(THIS_FOLDER + '/DB/' 'base_de_datos.json') #-> A ese directorio le sumamos el del archivo. La ruta total se almacena en my_file
# #Aquí "os" detecta el directorio donde se ejecuta nuestro archivo python es decir en este caso "models.py" y a partir de allí almacena esta ruta en THIS_FOLDER. Luego ya sabiendo que la ruta es donde está "models.py" bastará agregarle el directorio DB y finalmente indicar el nombre de archivo.
# # --> Cargar archivo JSON   
# with open (my_file, "r") as f: #->Abrimos pasando como arg la variable my_file que contiene ruta completa Y ALMACENAMOS EN "f"
#     datos = json.load(f) #-> Almacenamos en la variable "datos" la interpreteación de nuestro JSON que está almacenado en "f"
# datos_personas = datos['Personas']
# # --> Cerrar lectura Archivo JSON
# f.close()
# #BLOQUE CLASE PERSONA Y CRUD
# class Persona(object):
#     contador_id = datos["Configuraciones"][0]["contador_id_db"]
#     def __init__(self, nombre, apellido, apodo, telefono, direccion):
#         print("El contador está en: ", Persona.contador_id)
#         self.id = Persona.contador_id #Atriuto id es igual a la variable
#         self.nombre = nombre
#         self.apellido = apellido
#         self.apodo = apodo
#         self.telefono = telefono
#         self.direccion = direccion
#     #Método CREATE -> Crear una nueva persona o contacto de la base de datos
#     def crear_contacto(self):    
#         with open (my_file, "w") as modid:
#             datos["Configuraciones"][0]["contador_id_db"]+=1#Cambiamos el valor de "contador_id_db" por el de la id +1
#             json.dump(datos, modid, indent=4)
#             modid.close() # Cerramos el JSON
#             print("El contador está ahora en: ", datos["Configuraciones"][0]["contador_id_db"])
#             #Una vez modificamos el valor de la variable en el JSON
#             #Lo hacemos también en la variable de CLASE Personas:
#             Persona.contador_id +=1
#         #Creamos nueva instancia
#             nueva_persona = Persona(
#                 self.nombre,
#                 self.apellido,
#                 self.apodo,
#                 self.telefono, 
#                 self.direccion).__dict__ #Guardamos la nueva persona es decir "instancia" dentro de la variable "nueva_persona" como DICCIONARIO
#                 #Abrimos nuevamente el JSON pero en modo de escritura "w" y con un nuevo nombre de instancia "fr"
#             with open (my_file, "w") as fr: #->Estamos abriendo exactamente de la misma forma pero con "w"
#                 datos['Personas'].append(nueva_persona) #->Entramos a los valores de la clave "Personas" que son Lista y añadimos el nuevo objeto (diccionario)
#                 json.dump(datos, fr, indent =4) #Finalmente almacenamos en la base de datos argumentando ademas un identado.
#                 #Cerramos el JSON
#                 fr.close()
#     #Método READ -> Leer una persona o contacto de la base de datos
#     def leer_contacto(atr, valor):
#         encontradas = {} #Creamos un diccionario para almacenar los resultados
#         for persona in datos["Personas"]: #Cada "indice" es un diccionario de persona
#             if persona[atr] == valor or valor == 'all': #Si el atributo de ese diccionario es igual al que pasamos
#                 #Obtenemos el indice de esa persona
#                 indice = datos["Personas"].index(persona) #La variable toma el valor de la posición de la persona
#                 #Guardamos en el diccionario nuevo
#                 encontradas[indice] = persona #Se añade cada persona encontrada con index como clave
#         return (encontradas) #Retornamos los datos encontrados
    
#     #Método UPDATE -> Actualizar o modificar un dato de algún contacto en la bd
#     def actualizar_contacto(id, atr, nuevo_valor):
#         for persona in datos["Personas"]: #Cada "indice" es un diccionario de persona
#             if persona["id"] == id: #Si el "id" de ese diccionario es igual al arguemento id
#                 print (persona) #Imprime el diccionario
                
#                 #Obtenemos el indice de esa persona
#                 indice = datos["Personas"].index(persona) #La variable toma el valor de la posición de la persona
#                 datos["Personas"][indice][atr] = nuevo_valor #Accedemos a ese diccionario> clave y cambiamos su valor
#                 print (datos["Personas"][indice][atr]) #Imprimimos para confirmar el cambio en "datos" (lectura)
                
#                 #Ahora es momento de guardar el cambio en la base de datos JSON:
#                 with open (my_file, "w") as modificar: #->Estamos abriendo exactamente de la misma forma pero con "w"
#                     json.dump(datos, modificar, indent =4) #Finalmente almacenamos en la base de datos argumentando ademas un identado.
#                 #Cerramos el JSON
#                     modificar.close()  
            
#     #Método DELETE -> Borrar una persona o contacto de la base de datos
#     def eliminar_contacto(id):
#         for persona in datos["Personas"]: #Cada "indice" es un diccionario de persona
#             if persona["id"] == id: #Si el "id" de ese diccionario es igual al arguemento id
#                 print ("Se va a borrar: ", persona) #Imprime el diccionario
                
#                 #Obtenemos el indice de esa persona
#                 indice = datos["Personas"].index(persona) #La variable toma el valor de la posición de la persona
#                 datos["Personas"].pop(indice) #Borramos usando el método de listas .pop()
#                 #Guardamos los cambios en el JSON
#                 with open (my_file, "w") as eliminar: #->Estamos abriendo exactamente de la misma forma pero con "w"
#                     json.dump(datos, eliminar, indent =4) #Finalmente almacenamos en la base de datos argumentando ademas un identado.
#                 #Cerramos el JSON
#                     eliminar.close()  