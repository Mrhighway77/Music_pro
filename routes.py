from flask import Blueprint, jsonify
from flask.views import MethodView
from models import Producto

# Crear un Blueprint para las rutas relacionadas con los productos
productos_bp = Blueprint('productos', __name__, url_prefix='/productos')

# Definir la clase ProductoListView para manejar las solicitudes GET de la lista de productos
class ProductoListView(MethodView):
    def get(self):
        productos = Producto.query.all()
        productos = [producto.serialize() for producto in productos]
        return jsonify(productos)

# Definir la clase ProductoView para manejar las solicitudes GET de un producto específico
class ProductoView(MethodView):
    def get(self, id):
        producto = Producto.query.get(id)
        if producto:
            return jsonify(producto.serialize())
        else:
            return jsonify({"mensaje": "Producto no encontrado"}), 404

# Agregar las rutas al Blueprint de productos
productos_bp.add_url_rule('', view_func=ProductoListView.as_view('productos'))
productos_bp.add_url_rule('/<int:id>', view_func=ProductoView.as_view('producto'))
