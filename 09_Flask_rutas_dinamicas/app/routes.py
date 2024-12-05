from flask import  jsonify, request
from app import app
from app.frutas import frutas

@app.route('/')
def index():
    return jsonify({"message": "Bienvenid@s al endpoint Frutas"}), 200

# @app.route('/frutas')
# def ver_frutas():
#     if not frutas:
#         return jsonify({"error": "error al obtener las frutas"}), 500
    
#     return jsonify(frutas), 200

@app.route('/frutas', methods=['GET'])
def ver_frutas():
    precio_param = request.args.get('importer', None)

    if not frutas:
        return jsonify({"error": "error al obtener las frutas"}), 500
    
    if precio_param is not None:
        try:
            precio = float(precio_param)
        except ValueError:
            return jsonify({"error": "el valor del precio no es valido"}), 400
        
        fruta_exacta = next((fruta for fruta in frutas if fruta['importe'] == precio), None)

        if fruta_exacta is not None:
            return jsonify(fruta_exacta), 200
        
        return jsonify({"error": "no se ha encontrado un producto con ese precio"}), 404
    
    return jsonify(frutas), 200

@app.route('/frutas/<int:id>', methods=['GET'])
def ver_frutas_por_id(id):
    fruta_econtrada = next((fruta for fruta in frutas if fruta['id'] == id), None)

    if fruta_econtrada:
        return jsonify(fruta_econtrada), 200
    else:
        return jsonify({"error": "Fruta no encontrada"}), 404
    
@app.route('/frutas/nombre/<nombre>', methods=['GET'])
def ver_frutas_nombre(nombre):
    nombre = nombre.lower()

    if not frutas:
        return jsonify({"error": "no se encontraron productos"}), 404

    frutas_filtradas = [fruta for fruta in frutas if nombre in fruta['nombre'].lower()]    
    return jsonify(frutas_filtradas), 200

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "ruta no disponible"}), 404