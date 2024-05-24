
from flask import Flask, redirect, request, render_template, url_for, flash #Importamos clase Flask, objeto request de flask (librería)
from config import config
from flask_mysqldb import MySQL

import mysql.connector


from models.ModelUser import ModelUser 

from models.entities.User import User

app = Flask(__name__) #Creamos una app instanciando la clase Flask (automáticamente el nombre de la app)
#Rutas - (argumentos: Url) - Función

db = MySQL(app)

@app.route('/')
def index():
    return render_template(('index.html'))

#@app.route('/login', methods = ['GET', 'POST']) #Decoramos con método de app que es una instancia de la clase Flask y argumentamos "slash"
#def inicio(): #Definimos una función llamada Inicio
 #   if request.method == 'POST':
  #       print(request.form['inputUsername'])
   #      print(request.form['inputPassword'])
    #     return render_template('auth/login.html')
    #else:
     #   return render_template('auth/login.html') #Retornornamos el template usando RENDER_TEMPLATE()


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
        # print(request.form['inputUsername'])
        # print(request.form['inputPassword'])
        user = User(0,request.form['inputUsername'],request.form['inputPassword'])
        logged_user = ModelUser.login(db,user)
        if logged_user is not None:
            if logged_user.password:  # Suponiendo que esto verifica si la contraseña no está vacía
                return redirect(url_for('home.html'))
            else:
                flash("Clave Inválida")
                return render_template('auth/login.html')
        else:
            flash("Usuario no encontrado")
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html') #Retornornamos el template usando RENDER_TEMPLATE()

@app.route('/home')
def home():
    return render_template('home.html')



    db = MYSQL_DB.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="flask_login"
    )

if __name__=='__main__':
    app.config.from_object(config['development'])
    app.run(debug=True)
