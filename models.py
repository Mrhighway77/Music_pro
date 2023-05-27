# Importar  SQLAlchemy para trabajar con la base de datos
from flask_sqlalchemy import SQLAlchemy
from app import db

# Crear una instancia de SQLAlchemy
db = SQLAlchemy()

# Definir la clase Producto como un modelo de la base de datos
class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    serie_producto = db.Column(db.String(50), nullable=False)
    marca = db.Column(db.String(50), nullable=False)
    codigo = db.Column(db.String(50), nullable=False)
    cliente = db.Column(db.String(100), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "serie_producto": self.serie_producto,
            "marca": self.marca,
            "codigo": self.codigo,
            "cliente": self.cliente
        }
