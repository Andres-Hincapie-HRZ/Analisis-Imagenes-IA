from flask import Flask, render_template, request, jsonify, redirect, url_for
import os
import base64
import requests
import json
from werkzeug.utils import secure_filename
from PIL import Image
import io

aplicacion = Flask(__name__)
aplicacion.config['SECRET_KEY'] = 'tu_clave_secreta_aqui'
aplicacion.config['CARPETA_SUBIDAS'] = 'static/subidas'
aplicacion.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB tamaño máximo de archivo

# Crear directorio de subidas si no existe
os.makedirs(aplicacion.config['CARPETA_SUBIDAS'], exist_ok=True)

# Configuración de la API
CLAVE_API_OPENROUTER = "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"
URL_OPENROUTER = "https://openrouter.ai/api/v1/chat/completions"

def procesar_imagen_con_inteligencia_artificial(ruta_imagen, pregunta):
    """Envía la imagen y pregunta a la API de OpenRouter"""
    try:
        # Leer y codificar la imagen en base64
        with open(ruta_imagen, "rb") as archivo_imagen:
            imagen_codificada = base64.b64encode(archivo_imagen.read()).decode('utf-8')
        
        # Detectar el formato de la imagen
        with Image.open(ruta_imagen) as img:
            formato_imagen = img.format.lower() if img.format else 'jpeg'
            # Mapear formatos comunes
            if formato_imagen == 'jpeg':
                mime_type = 'image/jpeg'
            elif formato_imagen == 'png':
                mime_type = 'image/png'
            elif formato_imagen == 'webp':
                mime_type = 'image/webp'
            elif formato_imagen == 'gif':
                mime_type = 'image/gif'
            else:
                mime_type = 'image/jpeg'  # Por defecto JPEG
        
        # Preparar el mensaje para la API
        mensaje = {
            "model": "meta-llama/llama-4-maverick:free",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": f"Analiza esta imagen y responde a la siguiente pregunta: {pregunta}"
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:{mime_type};base64,{imagen_codificada}"
                            }
                        }
                    ]
                }
            ],
            "max_tokens": 1000
        }
        
        # Enviar solicitud a la API
        encabezados = {
            "Authorization": f"Bearer {CLAVE_API_OPENROUTER}",
            "Content-Type": "application/json",
            "HTTP-Referer": "http://localhost:5000",
            "X-Title": "Análisis de Imágenes con IA"
        }
        
        print(f"Enviando solicitud a OpenRouter con modelo: {mensaje['model']}")
        print(f"Tamaño de imagen: {len(imagen_codificada)} caracteres")
        
        respuesta = requests.post(URL_OPENROUTER, headers=encabezados, json=mensaje)
        print(f"Respuesta de API - Status: {respuesta.status_code}")
        
        if respuesta.status_code == 200:
            datos = respuesta.json()
            return datos['choices'][0]['message']['content']
        else:
            try:
                error_data = respuesta.json()
                error_msg = error_data.get('error', {}).get('message', 'Error desconocido')
                print(f"Error de API - Status: {respuesta.status_code}, Error: {error_msg}")
                return f"Error de la API: {error_msg}"
            except Exception as e:
                print(f"Error al procesar respuesta de API - Status: {respuesta.status_code}, Texto: {respuesta.text}")
                return f"Error al procesar la imagen: {respuesta.status_code} - {respuesta.text}"
            
    except Exception as e:
        return f"Error al procesar la imagen: {str(e)}"

@aplicacion.route('/')
def pagina_principal():
    return render_template('index.html')

@aplicacion.route('/cargar_imagen', methods=['POST'])
def cargar_imagen():
    try:
        # Obtener imagen del formulario
        if 'imagen' not in request.files:
            return jsonify({'error': 'No se seleccionó ninguna imagen'}), 400
        
        archivo = request.files['imagen']
        if archivo.filename == '':
            return jsonify({'error': 'No se seleccionó ninguna imagen'}), 400
        
        # Debug: imprimir información del archivo
        print(f"Archivo recibido: {archivo.filename}, tipo: {archivo.content_type}")
        
        if archivo:
            try:
                # Guardar archivo primero
                nombre_archivo = secure_filename(archivo.filename)
                ruta_archivo = os.path.join(aplicacion.config['CARPETA_SUBIDAS'], nombre_archivo)
                archivo.save(ruta_archivo)
                
                # Validar formato de imagen después de guardar
                with Image.open(ruta_archivo) as img:
                    formato_imagen = img.format.lower() if img.format else 'unknown'
                    formatos_validos = ['jpeg', 'jpg', 'png', 'webp', 'gif']
                    
                    if formato_imagen not in formatos_validos:
                        # Eliminar archivo si no es válido
                        os.remove(ruta_archivo)
                        return jsonify({'error': 'Formato de imagen no soportado. Use JPEG, PNG, WebP o GIF.'}), 400
                    
                    # Redimensionar imagen para vista previa
                    img.thumbnail((400, 400), Image.Resampling.LANCZOS)
                    img.save(ruta_archivo)
                
                return jsonify({
                    'exito': True,
                    'nombre_archivo': nombre_archivo,
                    'mensaje': 'Imagen cargada exitosamente'
                })
            except Exception as e:
                # Eliminar archivo si hay error
                if os.path.exists(ruta_archivo):
                    os.remove(ruta_archivo)
                return jsonify({'error': f'Error al procesar la imagen: {str(e)}'}), 400
    
    except Exception as e:
        return jsonify({'error': f'Error al cargar la imagen: {str(e)}'}), 500

@aplicacion.route('/preguntar', methods=['POST'])
def preguntar():
    try:
        datos = request.get_json()
        nombre_archivo = datos.get('nombre_archivo')
        pregunta = datos.get('pregunta')
        
        if not nombre_archivo or not pregunta:
            return jsonify({'error': 'Faltan datos requeridos'}), 400
        
        ruta_imagen = os.path.join(aplicacion.config['CARPETA_SUBIDAS'], nombre_archivo)
        
        if not os.path.exists(ruta_imagen):
            return jsonify({'error': 'Imagen no encontrada'}), 404
        
        # Procesar con IA
        respuesta = procesar_imagen_con_inteligencia_artificial(ruta_imagen, pregunta)
        
        return jsonify({
            'exito': True,
            'respuesta': respuesta
        })
    
    except Exception as e:
        return jsonify({'error': f'Error al procesar la pregunta: {str(e)}'}), 500

if __name__ == '__main__':
    aplicacion.run(debug=True, host='0.0.0.0', port=5000)