
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, jsonify
import urllib.parse

# Módulo sqlAlchemy es para que me permite acceder y manipular la DB
from flask_sqlalchemy import SQLAlchemy

# Módulo sqlAlchemy es para que me permite acceder y manipular la DB
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

# Módulo cors es para que me permite acceder desde el frontend al backend
from flask_cors import CORS

# Crea el objeto app
app = Flask(__name__)

# permite acceder desde el frontend al backend
CORS(app)

# acjustar user:pass@url dependiendo del deploy
# contraseña => URL encode, ya que contiene @ que tambien se usa para señalizar URL del server
_pass = urllib.parse.quote("J3r3m!@s33.3")

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+mysqlconnector://bibliofilos23529:{_pass}@bibliofilos23529.mysql.pythonanywhere-services.com/bibliofilos23529$default"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Crea un objeto db, para informar a la app que se trabajará con sqlalchemy
db = SQLAlchemy(app)

# Definir tabla Usuario
class Usuario(db.Model):
    id_usuario = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    apellido = db.Column(db.String(50))
    nickname = db.Column(db.String(50))
    contrasena = db.Column(db.String(50))
    email = db.Column(db.String(50))
 #  libros = relationship('Libro', backref='colaborador')

    def __init__(self,nombre,apellido,nickname,contrasena,email):   #crea el constructor de la clase
        self.nombre=nombre
        self.apellido=apellido
        self.nickname=nickname
        self.contrasena=contrasena
        self.email=email
#-------------------------------------------------------------------------------------------------------------#
# Definir tabla Libro
class Libro(db.Model):
    id_libro = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(50))
    autor = db.Column(db.String(50))
    idioma = db.Column(db.String(50))
    edicion = db.Column(db.String(50))
    genero = db.Column(db.String(50))
    isbn = db.Column(db.Integer)
    imagen = db.Column(db.String(400))
    colaborador = db.Column(db.Integer, ForeignKey('usuario.id_usuario'))

    def __init__(self,titulo,autor,idioma,edicion,genero,isbn,imagen,colaborador):   #crea el constructor de la clase
        self.titulo=titulo
        self.autor=autor
        self.idioma=idioma
        self.edicion=edicion
        self.genero=genero
        self.isbn=isbn
        self.imagen=imagen
        self.colaborador=colaborador
#-------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------#
# Crea las tablas al ejecutarse la app
with app.app_context():
    db.create_all()

#rutas de acceso
# / Pagina de inicio
@app.route("/")
def index():
    return f'App Web para registrar y compartir libros entre bibliofilos.'

#-------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------#
# CREA un registro en la tabla Libro
@app.route("/registro_libro", methods=["POST"])
def registro_libro():

    titulo = request.json["titulo"]
    autor = request.json["autor"]
    idioma = request.json["idioma"]
    edicion = request.json["edicion"]
    genero = request.json["genero"]
    isbn = request.json["isbn"]
    imagen = request.json["imagen"]
    colaborador = request.json["imagen"]
    nuevo_registro=Libro(titulo,autor,idioma,edicion,genero,isbn,imagen,colaborador)
    db.session.add(nuevo_registro)
    db.session.commit()
    # {"titulo": "Harry Potter", ...} -> input tiene el atributo name="titulo"
    return "Solicitud de post recibida"

#-------------------------------------------------------------------------------------------------------------#
# CREA un registro en la tabla Usuario
@app.route("/registro_usuario", methods=["POST"])
def registro_usuario():

    nombre = request.json["nombre"]
    apellido = request.json["apellido"]
    nickname = request.json["nickname"]
    contrasena = request.json["contrasena"]
    email = request.json["email"]
    nuevo_registro=Usuario(nombre,apellido,nickname,contrasena,email)
    #print(nuevo_registro.__dict__)
    db.session.add(nuevo_registro)
    db.session.commit()
    # {"nombre": "Felipe", ...} -> input tiene el atributo name="nombre"
    return "Solicitud de post recibida"

#-------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------#
# RETORNAR todos los registros de libros en un Json
@app.route("/ver_libro",  methods=['GET'])
def ver_libro():
    # Consultar en la tabla todos los registros
    # all_registros -> lista de objetos
    all_registros = Libro.query.all()

    # Lista de diccionarios
    data_serializada = []

    for objeto in all_registros:
        data_serializada.append({"id_libro":objeto.id_libro, "titulo":objeto.titulo, "autor":objeto.autor, "idioma":objeto.idioma, "edicion":objeto.edicion, "genero":objeto.genero, "isbn":objeto.isbn, "imagen":objeto.imagen, "colaborador":objeto.colaborador})

    return jsonify(data_serializada)
#-------------------------------------------------------------------------------------------------------------#
# RETORNAR todos los registros de usuarios en un Json
@app.route("/ver_usuario",  methods=['GET'])
def ver_usuario():
    # Consultar en la tabla todos los registros
    # all_registros -> lista de objetos
    all_registros = Usuario.query.all()

    # Lista de diccionarios
    data_serializada = []

    for objeto in all_registros:
        data_serializada.append({"id_usuario":objeto.id_usuario, "nombre":objeto.nombre, "apellido":objeto.apellido, "nickname":objeto.nickname,"contrasena":objeto.contrasena, "email":objeto.email})

    return jsonify(data_serializada)
#-------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------#
# MODIFICAR un registro de libros
@app.route('/update_libro/<id_libro>', methods=['PUT'])
def update_libro(id_libro):
    # Buscar el registro a modificar en la tabla por su id
    libro = Libro.query.get(id_libro)

    # {"titulo": "Harry Potter"} -> input tiene el atributo name="titulo"
    titulo = request.json["titulo"]
    autor = request.json["autor"]
    idioma = request.json["idioma"]
    edicion = request.json["edicion"]
    genero = request.json["genero"]
    isbn = request.json["isbn"]
    imagen = request.json["imagen"]
    colaborador = request.json["colaborador"]

    libro.titulo=titulo
    libro.autor=autor
    libro.idioma=idioma
    libro.edicion=edicion
    libro.genero=genero
    libro.isbn=isbn
    libro.imagen=imagen
    libro.colaborador=colaborador
    db.session.commit()

    data_serializada = [{"id_libro":libro.id_libro, "titulo":libro.titulo, "autor":libro.autor, "idioma":libro.idioma, "edicion":libro.edicion, "genero":libro.genero, "isbn":libro.isbn, "imagen":libro.imagen, "colaborador":libro.colaborador}]

    return jsonify(data_serializada)
#-------------------------------------------------------------------------------------------------------------#
# MODIFICAR un registro de usuarios
@app.route('/update_usuario/<id_usuario>', methods=['PUT'])
def update_usuario(id_usuario):
    # Buscar el registro a modificar en la tabla por su id
    usuario = Usuario.query.get(id_usuario)

    # {"nombre": "Felipe"} -> input tiene el atributo name="nombre"
    nombre = request.json["nombre"]
    apellido = request.json["apellido"]
    nickname = request.json["nickname"]
    contrasena = request.json["contrasena"]
    email = request.json["email"]

    usuario.nombre=nombre
    usuario.apellido=apellido
    usuario.nickname=nickname
    usuario.contrasena=contrasena
    usuario.email=email
    db.session.commit()

    data_serializada = [{"id_usuario":usuario.id_usuario, "nombre":usuario.nombre, "apellido":usuario.apellido, "nickname":usuario.nickname,"contrasena":usuario.contrasena, "email":usuario.email}]

    return jsonify(data_serializada)
#-------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------##-------------------------------------------------------------------------------------------------------------#
# BORRAR un registro de libros
@app.route('/borrar_libro/<id_libro>', methods=['DELETE'])
def borrar_libro(id_libro):
    print(id_libro)
    # Se busca al libro por id en la DB
    libro = Libro.query.get(id_libro)

    # Se elimina de la DB
    db.session.delete(libro)
    db.session.commit()

    data_serializada = [{"id_libro":libro.id_libro, "titulo":libro.titulo, "autor":libro.autor, "idioma":libro.idioma, "edicion":libro.edicion, "genero":libro.genero, "isbn":libro.isbn, "imagen":libro.imagen, "colaborador":libro.colaborador}]

    return jsonify(data_serializada)
#-------------------------------------------------------------------------------------------------------------#
# BORRAR un registro de usuarios
@app.route('/borrar_usuario/<id_usuario>', methods=['DELETE'])
def borrar_usuario(id_usuario):
    print(id_usuario)
    # Se busca al usuario por id en la DB
    usuario = Usuario.query.get(id_usuario)

    # Se elimina de la DB
    db.session.delete(usuario)
    db.session.commit()

    data_serializada = [{"id_usuario":usuario.id_usuario, "nombre":usuario.nombre, "apellido":usuario.apellido, "nickname":usuario.nickname,"contrasena":usuario.contrasena, "email":usuario.email}]

    return jsonify(data_serializada)
#-------------------------------------------------------------------------------------------------------------#

if __name__ == "__main__":
    app.run(debug=True)



