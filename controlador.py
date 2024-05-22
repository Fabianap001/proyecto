#Esto es el servidor 
from flask import Flask, redirect, request, render_template, url_for #Importamos clase Flask, objeto request de flask (librería)
from config import config
from flask_mysqldb import MySQL



app = Flask(__name__) #Creamos una app instanciando la clase Flask (automáticamente el nombre de la app)
#Rutas - (argumentos: Url) - Función

db = MySQL(app)

@app.route('/')
def index():
    return render_template(('index.html'))

@app.route('/login', methods = ['GET', 'POST']) #Decoramos con método de app que es una instancia de la clase Flask y argumentamos "slash"
def inicio(): #Definimos una función llamada Inicio
    if request.method == 'POST':
        print(request.form['inputEmail'])
        print(request.form['inputPassword'])
        return render_template('auth/login.html')
    else:
        return render_template('auth/login.html') #Retornornamos el template usando RENDER_TEMPLATE()


@app.route('/Inicio', methods = ['GET']) #Decoramos con método routes la próxima función argumentando la url "/agradecimiento"
def agradecer(): #Definimos una función llamada agradecer
    return 'Gracias pythones.net!' #Retorno de la función
#Iniciar app

#@app.route('/login')
#def index():
#    return redirect(url_for('login()'))

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        print(request.form['username'])
        print(request.form['password'])
        return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')


if __name__=='__main__':
    app.config.from_object(config['development'])
    app.run(debug=True)
