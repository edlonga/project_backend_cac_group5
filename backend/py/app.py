#  Importar las herramientas
# Acceder a las herramientas para crear la app web
from flask import Flask, request, jsonify, render_template

# Para manipular la DB
from flask_sqlalchemy import SQLAlchemy 

# Módulo cors es para que me permita acceder desde el frontend al backend
from flask_cors import CORS

# Crear la app

app = Flask(__name__)


# permita acceder desde el frontend al backend
CORS(app)


# Configurar a la app la DB
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://usuario:contraseña@localhost:3306/nombre_de_la_base_de_datos'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:1234@localhost:3306/bibliofilos_db_23529' # ACA VAN A IR LOS DATOS DEL SERVER EN PYTHON ANYWHERE, VER CLASE PYTHON... 9?

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Crear un objeto db, para informar a la app que se trabajará con sqlalchemy
db = SQLAlchemy(app)

#-------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------#
# Definir la tabla 1
class Libro(db.Model):
    id_libro = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(50))
    autor = db.Column(db.String(50))
    idioma = db.Column(db.String(50))
    edicion = db.Column(db.String(50))
    genero = db.Column(db.String(50))
    isbn = db.Column(db.Integer)
    imagen = db.Column(db.String(400))

    
    def __init__(self,titulo,autor,idioma,edicion,genero,isbn,imagen):   #crea el constructor de la clase
        self.titulo=titulo   # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.autor=autor
        self.idioma=idioma
        self.edicion=edicion
        self.genero=genero
        self.isbn=isbn
        self.imagen=imagen
#-------------------------------------------------------------------------------------------------------------#
# Definir la tabla 2
class Usuario(db.Model):
    id_usuario = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    apellido = db.Column(db.String(50))
    nickname = db.Column(db.String(50))
    email = db.Column(db.String(50))
    
    def __init__(self,nombre,apellido,nickname,email):   #crea el constructor de la clase
        self.nombre=nombre   # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.apellido=apellido
        self.nickname=nickname
        self.email=email
#-------------------------------------------------------------------------------------------------------------#
# Definir la tabla 3
class Roles(db.Model):
    id_rol = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer)
    id_libro = db.Column(db.Integer)
    rol_descripcion = db.Column(db.String(20))
    
    def __init__(self,id_usuario,id_libro,rol_descripcion):   #crea el constructor de la clase
        self.id_usuario=id_usuario   # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.id_libro=id_libro
        self.rol_descripcion=rol_descripcion
#-------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------#
# 8. Crear las tablas al ejecutarse la app
with app.app_context():
    db.create_all()

# Crear ruta de acceso
# / es la ruta de inicio
@app.route("/")
def index():
    return f'App Web para registrar nombres de libros, usuarios y roles'
    
#-------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------#
# CREAR un registro en la tabla Libro
@app.route("/registro_libro", methods=["POST"]) 
def registro_libro():

    titulo = request.json["titulo"]
    autor = request.json["autor"]
    idioma = request.json["idioma"]
    edicion = request.json["edicion"]
    genero = request.json["genero"]
    isbn = request.json["isbn"]
    imagen = request.json["imagen"]
    nuevo_registro=Libro(titulo,autor,idioma,edicion,genero,isbn,imagen)
    db.session.add(nuevo_registro) #COMO SE A QUE TABLA AGREGARLO? HAY QUE ACLARARLO EN ALGUN LADO, O SABE SOLO POR SER UN OBJETO LIBRO?
    db.session.commit()
    # {"titulo": "Harry Potter", ...} -> input tiene el atributo name="titulo"
    return "Solicitud de post recibida"
    
#-------------------------------------------------------------------------------------------------------------#
# CREAR un registro en la tabla Usuario
@app.route("/registro_usuario", methods=["POST"]) 
def registro_usuario():

    nombre = request.json["nombre"]
    apellido = request.json["apellido"]
    nickname = request.json["nickname"]
    email = request.json["email"]
    nuevo_registro=Usuario(nombre,apellido,nickname,email)
    #print(nuevo_registro.__dict__)
    db.session.add(nuevo_registro) #COMO SE A QUE TABLA AGREGARLO? HAY QUE ACLARARLO EN ALGUN LADO, O SABE SOLO POR SER UN OBJETO USUARIO?
    db.session.commit()
    # {"nombre": "Felipe", ...} -> input tiene el atributo name="nombre"
    return "Solicitud de post recibida"


#-------------------------------------------------------------------------------------------------------------#
# CREAR un registro en la tabla Rol
@app.route("/registro_roles", methods=['POST']) 
def registro_roles():
    # {"id_usuario": "25", ...} -> input tiene el atributo name="id_usuario"
    id_usuario = request.json["id_usuario"]
    id_libro = request.json["id_libro"]
    rol_descripcion = request.json["rol_descripcion"]
    nuevo_registro=Roles(id_usuario,id_libro,rol_descripcion)
    db.session.add(nuevo_registro) #COMO SE A QUE TABLA AGREGARLO? HAY QUE ACLARARLO EN ALGUN LADO, O SABE SOLO POR SER UN OBJETO ROL?
    db.session.commit()

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
        data_serializada.append({"id_libro":objeto.id_libro, "titulo":objeto.titulo, "autor":objeto.autor, "idioma":objeto.idioma, "edicion":objeto.edicion, "genero":objeto.genero, "isbn":objeto.isbn, "imagen":objeto.imagen})

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
        data_serializada.append({"id_usuario":objeto.id_usuario, "nombre":objeto.nombre, "apellido":objeto.apellido, "nickname":objeto.nickname, "email":objeto.email})

    return jsonify(data_serializada)
#-------------------------------------------------------------------------------------------------------------#
# RETORNAR todos los registros de roles en un Json
@app.route("/ver_roles",  methods=['GET'])
def ver_roles():
    # Consultar en la tabla todos los registros
    # all_registros -> lista de objetos
    all_registros = Roles.query.all()

    # Lista de diccionarios
    data_serializada = []
    
    for objeto in all_registros:
        data_serializada.append({"id_rol":objeto.id_rol, "id_usuario":objeto.id_usuario, "id_libro":objeto.id_libro, "rol_descripcion":objeto.rol_descripcion})

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

    libro.titulo=titulo
    libro.autor=autor
    libro.idioma=idioma
    libro.edicion=edicion
    libro.genero=genero
    libro.isbn=isbn
    libro.imagen=imagen
    db.session.commit()

    data_serializada = [{"id_libro":libro.id_libro, "titulo":libro.titulo, "autor":libro.autor, "idioma":libro.idioma, "edicion":libro.edicion, "genero":libro.genero, "isbn":libro.isbn, "imagen":libro.imagen}]
    
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
    email = request.json["email"]

    usuario.nombre=nombre
    usuario.apellido=apellido
    usuario.nickname=nickname
    usuario.email=email
    db.session.commit()

    data_serializada = [{"id_usuario":usuario.id_usuario, "nombre":usuario.nombre, "apellido":usuario.apellido, "nickname":usuario.nickname, "email":usuario.email}]
    
    return jsonify(data_serializada)
#-------------------------------------------------------------------------------------------------------------#
# MODIFICAR un registro de roles
@app.route('/update_rol/<id_rol>', methods=['PUT'])
def update_rol(id_rol):
    # Buscar el registro a modificar en la tabla por su id
    rol = Roles.query.get(id_rol)

    # {"id_usuario": "25"} -> input tiene el atributo name="id_usuario"
    id_usuario = request.json["id_usuario"]
    id_libro = request.json["id_libro"]
    rol_descripcion = request.json["rol_descripcion"]

    rol.id_usuario=id_usuario
    rol.id_libro=id_libro
    rol.rol_descripcion=rol_descripcion
    db.session.commit()

    data_serializada = [{"id_rol":rol.id_rol, "id_usuario":rol.id_usuario, "id_libro":rol.id_libro, "rol":rol.rol_descripcion}]
    
    return jsonify(data_serializada)
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

    data_serializada = [{"id_libro":libro.id_libro, "titulo":libro.titulo, "autor":libro.autor, "idioma":libro.idioma, "edicion":libro.edicion, "genero":libro.genero, "isbn":libro.isbn, "imagen":libro.imagen}]

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

    data_serializada = [{"id_usuario":usuario.id_usuario, "nombre":usuario.nombre, "apellido":usuario.apellido, "nickname":usuario.nickname, "email":usuario.email}]

    return jsonify(data_serializada)
#-------------------------------------------------------------------------------------------------------------#
# BORRAR un registro de roles
@app.route('/borrar_rol/<id_rol>', methods=['DELETE'])
def borrar_rol(id_rol):
    print(id_rol)
    # Se busca al rol por id en la DB
    rol = Roles.query.get(id_rol)

    # Se elimina de la DB
    db.session.delete(rol)
    db.session.commit()

    data_serializada = [{"id_rol":rol.id_rol, "id_usuario":rol.id_usuario, "id_libro":rol.id_libro, "rol":rol.rol_descripcion}]

    return jsonify(data_serializada)



if __name__ == "__main__":
    app.run(debug=True)