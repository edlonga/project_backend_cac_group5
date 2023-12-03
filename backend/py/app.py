#  Importar las herramientas
# Acceder a las herramientas para crear la app web
from flask import Flask, request, jsonify

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

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:1234@localhost:3306/db_23529' # ACA VAN A IR LOS DATOS DEL SERVER EN PYTHON ANYWHERE, VER CLASE PYTHON... 9?

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Crear un objeto db, para informar a la app que se trabajará con sqlalchemy
db = SQLAlchemy(app)

#-------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------#
# Definir la tabla 1
class Libro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(50))
    autor = db.Column(db.String(50))
    idioma = db.Column(db.String(50))
    edicion = db.Column(db.String(50))
    categoria = db.Column(db.String(50))
    isbn = db.Column(db.Integer)
    imagen = db.Column(db.String(400))

    def __init__(self,titulo,autor,idioma,edicion,categoria,isbn,imagen):   #crea el constructor de la clase
        self.titulo=titulo   # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.autor=autor
        self.idioma=idioma
        self.edicion=edicion
        self.categoria=categoria
        self.isbn=isbn
        self.imagen=imagen
#-------------------------------------------------------------------------------------------------------------#
# Definir la tabla 2
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
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
class Rol(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer)
    id_libro = db.Column(db.Integer)
    rol = db.Column(db.String(20))

    def __init__(self,id_usuario,id_libro,rol):   #crea el constructor de la clase
        self.id_usuario=id_usuario   # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.id_libro=id_libro
        self.rol=rol
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
@app.route("/registro_libro", methods=['POST']) 
def registro_libro():
    # {"titulo": "Harry Potter", ...} -> input tiene el atributo name="titulo"
    titulo = request.json["titulo"]
    autor = request.json["autor"]
    idioma = request.json["idioma"]
    edicion = request.json["edicion"]
    categoria = request.json["categeoria"]
    isbn = request.json["isbn"]
    imagen = request.json["imagen"]
    nuevo_registro=Libro(titulo,autor,idioma,edicion,categoria,isbn,imagen)
    db.session.add(nuevo_registro) #COMO SE A QUE TABLA AGREGARLO? HAY QUE ACLARARLO EN ALGUN LADO, O SABE SOLO POR SER UN OBJETO LIBRO?
    db.session.commit()

    return "Solicitud de post recibida"
#-------------------------------------------------------------------------------------------------------------#
# CREAR un registro en la tabla Usuario
@app.route("/registro_usuario", methods=['POST']) 
def registro_usuario():
    # {"nombre": "Felipe", ...} -> input tiene el atributo name="nombre"
    nombre = request.json["nombre"]
    apellido = request.json["apellido"]
    nickname = request.json["nickname"]
    email = request.json["email"]
    nuevo_registro=Usuario(nombre,apellido,nickname,email)
    db.session.add(nuevo_registro) #COMO SE A QUE TABLA AGREGARLO? HAY QUE ACLARARLO EN ALGUN LADO, O SABE SOLO POR SER UN OBJETO USUARIO?
    db.session.commit()

    return "Solicitud de post recibida"
#-------------------------------------------------------------------------------------------------------------#
# CREAR un registro en la tabla Rol
@app.route("/registro_rol", methods=['POST']) 
def registro_rol():
    # {"id_usuario": "25", ...} -> input tiene el atributo name="id_usuario"
    id_usuario = request.json["id_usuario"]
    id_libro = request.json["id_libro"]
    rol = request.json["rol"]
    nuevo_registro=Rol(id_usuario,id_libro,rol)
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
        data_serializada.append({"id":objeto.id, "titulo":objeto.titulo, "autor":objeto.autor, "idioma":objeto.idioma, "edicion":objeto.edicion, "categoria":objeto.categoria, "isbn":objeto.isbn, "imagen":objeto.imagen})

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
        data_serializada.append({"id":objeto.id, "nombre":objeto.nombre, "apellido":objeto.apellido, "nickname":objeto.nickname, "email":objeto.email})

    return jsonify(data_serializada)
#-------------------------------------------------------------------------------------------------------------#
# RETORNAR todos los registros de roles en un Json
@app.route("/ver_rol",  methods=['GET'])
def ver_rol():
    # Consultar en la tabla todos los registros
    # all_registros -> lista de objetos
    all_registros = Rol.query.all()

    # Lista de diccionarios
    data_serializada = []
    
    for objeto in all_registros:
        data_serializada.append({"id":objeto.id, "id_usuario":objeto.id_usuario, "id_libro":objeto.id_libro, "rol":objeto.rol})

    return jsonify(data_serializada)
#-------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------#
# MODIFICAR un registro de libros
@app.route('/update_libro/<id>', methods=['PUT'])
def update_libro(id):
    # Buscar el registro a modificar en la tabla por su id
    libro = Libro.query.get(id)

    # {"titulo": "Harry Potter"} -> input tiene el atributo name="titulo"
    titulo = request.json["titulo"]
    autor = request.json["autor"]
    idioma = request.json["idioma"]
    edicion = request.json["edicion"]
    categoria = request.json["categeoria"]
    isbn = request.json["isbn"]
    imagen = request.json["imagen"]

    libro.titulo=titulo
    libro.autor=autor
    libro.idioma=idioma
    libro.edicion=edicion
    libro.categoria=categoria
    libro.isbn=isbn
    libro.imagen=imagen
    db.session.commit()

    data_serializada = [{"id":libro.id, "titulo":libro.titulo, "autor":libro.autor, "idioma":libro.idioma, "edicion":libro.edicion, "categoria":libro.categoria, "isbn":libro.isbn, "imagen":libro.imagen}]
    
    return jsonify(data_serializada)
#-------------------------------------------------------------------------------------------------------------#
# MODIFICAR un registro de usuarios
@app.route('/update_usuario/<id>', methods=['PUT'])
def update_usuario(id):
    # Buscar el registro a modificar en la tabla por su id
    usuario = Usuario.query.get(id)

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

    data_serializada = [{"id":usuario.id, "nombre":usuario.nombre, "apellido":usuario.apellido, "nickname":usuario.nickname, "email":usuario.email}]
    
    return jsonify(data_serializada)
#-------------------------------------------------------------------------------------------------------------#
# MODIFICAR un registro de roles
@app.route('/update_rol/<id>', methods=['PUT'])
def update_rol(id):
    # Buscar el registro a modificar en la tabla por su id
    rol = Rol.query.get(id)

    # {"id_usuario": "25"} -> input tiene el atributo name="id_usuario"
    id_usuario = request.json["id_usuario"]
    id_libro = request.json["id_libro"]
    rol = request.json["rol"]

    rol.id_usuario=id_usuario
    rol.id_libro=id_libro
    rol.rol=rol
    db.session.commit()

    data_serializada = [{"id":rol.id, "id_usuario":rol.id_usuario, "id_libro":rol.id_libro, "rol":rol.rol}]
    
    return jsonify(data_serializada)
#-------------------------------------------------------------------------------------------------------------##-------------------------------------------------------------------------------------------------------------#
# BORRAR un registro de libros
@app.route('/borrar_libro/<id>', methods=['DELETE'])
def borrar_libro(id):
    print(id)
    # Se busca al libro por id en la DB
    libro = Libro.query.get(id)

    # Se elimina de la DB
    db.session.delete(libro)
    db.session.commit()

    data_serializada = [{"id":libro.id, "titulo":libro.titulo, "autor":libro.autor, "idioma":libro.idioma, "edicion":libro.edicion, "categoria":libro.categoria, "isbn":libro.isbn, "imagen":libro.imagen}]

    return jsonify(data_serializada)
#-------------------------------------------------------------------------------------------------------------#
# BORRAR un registro de usuarios
@app.route('/borrar_usuario/<id>', methods=['DELETE'])
def borrar_usuario(id):
    print(id)
    # Se busca al usuario por id en la DB
    usuario = Usuario.query.get(id)

    # Se elimina de la DB
    db.session.delete(usuario)
    db.session.commit()

    data_serializada = [{"id":usuario.id, "nombre":usuario.nombre, "apellido":usuario.apellido, "nickname":usuario.nickname, "email":usuario.email}]

    return jsonify(data_serializada)
#-------------------------------------------------------------------------------------------------------------#
# BORRAR un registro de roles
@app.route('/borrar_rol/<id>', methods=['DELETE'])
def borrar_rol(id):
    print(id)
    # Se busca al rol por id en la DB
    rol = Rol.query.get(id)

    # Se elimina de la DB
    db.session.delete(rol)
    db.session.commit()

    data_serializada = [{"id":rol.id, "id_usuario":rol.id_usuario, "id_libro":rol.id_libro, "rol":rol.rol}]

    return jsonify(data_serializada)

if __name__ == "__main__":
    app.run(debug=True)