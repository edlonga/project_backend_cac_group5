-- Active: 1698240975080@@localhost@3306@bibliofilos
CREATE DATABASE bibliofilos;

use bibliofilos;

CREATE TABLE usuario(
    id_usuario INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    nickname VARCHAR(50) NOT NULL,
    correo VARCHAR(50) NOT NULL
);

CREATE TABLE libro(
    id_libro INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    titulo VARCHAR(50) NOT NULL,
    autor VARCHAR(50) NOT NULL,
    idioma VARCHAR(50) NOT NULL,
    edicion VARCHAR(50) NOT NULL,
    genero VARCHAR(50) NOT NULL,
    ISBN INT DEFAULT 0,
    imagen VARCHAR(50) NOT NULL
);

CREATE TABLE roles(
    id_rol INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    id_usuario INT,
    id_libro INT,
    rol_descripcion VARCHAR(100) NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario),
    FOREIGN KEY (id_libro) REFERENCES libro(id_libro)
    );