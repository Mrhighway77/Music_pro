## Proyecto de Integración 
*API tienda y API FakeTransbank*

*Ambas APIS están realizadas con Python Flask, por lo que para levantar ambos host son los siguientes pasos:*
1. Tener instalado Python
2. Ejecutar en terminal:  pip install flask


### Archivo app.py
* Este archivo contiene la API de la tienda, una vez que se hayan hecho los pasos anteriores, en la terminal de este se ejecuta el comando: python app.py
* Debe ser este el Host: http://127.0.0.1:3000
  

### Archivo app2.py
* Este archivo contiene la API FakeTransbank, una vez que se hayan hecho los pasos anteriores, en la terminal de este se ejecuta los comandos en este orden: 
    * pip install requests 
    * python app2.py 
* Debe ser el Host: http://127.0.0.1:4000
  
### Uso de Endpoints
#### app.py
*Para la API de la tienda se utilizan 2 endpoint, para llamar a los productos o para llamar a un productos específico.*
* Para llamar a todos los productos http://127.0.0.1:3000/productos
* Para llamar a un producto http://127.0.0.1:3000/productos/1 
    * El último valor corresponde al id del producto 

#### app2.py
*Para la API FakeTransbank se utilizan 2 endopint, para llamar y revisar las cuentas y para ver la compra.*
* Para llamar a todas las cuentas http://127.0.0.1:4000/cuentas
* Para llamar a la compra http://127.0.0.1:4000/compra
  
### Método POST
*Para realizar la compra, http://127.0.0.1:4000/compra , en el método POST se debe agregar en el Body del Postman lo siguiente:*
­∼∼∼
{
  "num_tarjeta": "9999-8888-7777",
  "clave": "1234",
  "producto_id": 1
}
∼∼∼
*Cabe recalcar que es un ejemplo. Se puede cambiar el número de tarjeta, clave y id del producto*

### Métodos PUT, POST y DELETE
*En los productos, se pueden agregar, actualizar y borrar productos del listado, en cada uno de los métodos en el Body del Postman se debe agregar:*
∼∼∼
{
        "codigo": "PM234",
        "id": 11,
        "marca": "Marshall",
        "nombre": "Amplificador de guitarra XXX",
        "precio": 2500000,
        "serie_producto": "AMP001"
    }
∼∼∼
*Cabe recalcar que es un ejemplo. Se puede modificar el código, id, marca, nombre, precio y serie del producto*