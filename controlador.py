#Esto es el servidor 
from flask import Flask, request, render_template #Importamos clase Flask, objeto request de flask (librería)
app = Flask(__name__) #Creamos una app instanciando la clase Flask (automáticamente el nombre de la app)
#Rutas - (argumentos: Url) - Función
@app.route('/', methods = ['GET', 'POST']) #Decoramos con método de app que es una instancia de la clase Flask y argumentamos "slash"
def inicio(): #Definimos una función llamada Inicio
    if request.method == 'POST':
        pass
    else:
        return render_template('/index.html') #Retornornamos el template usando RENDER_TEMPLATE()
@app.route('/agradecimiento', methods = ['GET']) #Decoramos con método routes la próxima función argumentando la url "/agradecimiento"
def agradecer(): #Definimos una función llamada agradecer
    return 'Gracias pythones.net!' #Retorno de la función
#Iniciar app
if __name__ == '__main__': #Condicional de que si la aplicación ejecutada se coincide al nombre de la aplicación
    app.run('127.0.0.1', 5000, debug=True) #Método que inicia la app con la dirección, puertos y modo de argumentos