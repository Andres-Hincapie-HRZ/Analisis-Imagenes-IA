# 🖼️ Análisis de Imágenes con Inteligencia Artificial

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.0+-green?style=for-the-badge&logo=flask&logoColor=white)
![OpenRouter](https://img.shields.io/badge/OpenRouter-AI-orange?style=for-the-badge&logo=openai&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

**Una aplicación web moderna que permite analizar imágenes usando inteligencia artificial de última generación**

[🚀 Instalación](#-instalación) • [📖 Uso](#-uso) • [🔧 Configuración](#-configuración) • [📁 Estructura](#-estructura-del-proyecto)

</div>

---

## ✨ Características Principales

### 🎯 **Funcionalidades Avanzadas**
- 🖼️ **Carga Intuitiva**: Arrastra y suelta, selección manual o pegado desde portapapeles
- 🔍 **Vista Previa Instantánea**: Visualiza las imágenes antes del análisis
- 🤖 **IA de Última Generación**: Utiliza modelos avanzados de OpenRouter AI
- ⚡ **Procesamiento Rápido**: Análisis optimizado con redimensionamiento automático
- 🎨 **Interfaz Futurista**: Diseño azul neón con efectos visuales modernos

### 📱 **Experiencia de Usuario**
- 📱 **Totalmente Responsive**: Funciona perfectamente en móviles, tablets y escritorio
- 🎭 **Interfaz Intuitiva**: Diseño limpio y fácil de usar
- ⚡ **Tiempo Real**: Respuestas instantáneas con indicadores de carga
- 🔄 **Gestión de Estado**: Control completo del flujo de trabajo

### 🛡️ **Seguridad y Rendimiento**
- 🔒 **Validación de Archivos**: Verificación de formatos y tamaños
- 📏 **Límites Inteligentes**: Máximo 16MB por archivo
- 🗂️ **Gestión de Archivos**: Almacenamiento temporal seguro
- 🧹 **Limpieza Automática**: Eliminación de archivos temporales

---

## 🚀 Instalación

### 📋 Prerrequisitos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Conexión a internet (para la API de OpenRouter)

### ⚙️ Pasos de Instalación

1. **Clona o descarga el proyecto**
   ```bash
   git clone <url-del-repositorio>
   cd Proyecto_Python
   ```

2. **Instala las dependencias**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecuta la aplicación**
   ```bash
   python app.py
   ```

4. **Abre tu navegador**
   ```
   http://localhost:5000
   ```

### 🐳 Instalación con Docker (Opcional)
```bash
# Construir la imagen
docker build -t analisis-imagenes-ia .

# Ejecutar el contenedor
docker run -p 5000:5000 analisis-imagenes-ia
```

---

## 📖 Uso

### 🎯 Flujo de Trabajo

1. **📤 Cargar Imagen**
   - Arrastra y suelta una imagen en el área designada
   - Haz clic en "Seleccionar Imagen" para buscar archivos
   - Usa `Ctrl+V` para pegar desde el portapapeles

2. **❓ Hacer Preguntas**
   - Escribe tu pregunta en el área de texto
   - Haz clic en "Analizar Imagen"
   - Espera la respuesta de la IA

3. **🔄 Gestionar Contenido**
   - Usa "Limpiar Todo" para reiniciar
   - Cambia de imagen en cualquier momento

### 💡 Ejemplos de Preguntas Efectivas

#### 🔍 **Análisis General**
- "¿Qué objetos principales veo en esta imagen?"
- "Describe la escena completa"
- "¿Cuál es el tema principal de esta imagen?"

#### 🎨 **Análisis Visual**
- "¿Qué colores predominan en la imagen?"
- "¿Cómo es la iluminación de la escena?"
- "¿Qué texturas puedo identificar?"

#### 👥 **Análisis de Personas**
- "¿Hay personas en la imagen? ¿Qué están haciendo?"
- "¿Cuántas personas aparecen?"
- "¿Cómo están vestidas las personas?"

#### 🏢 **Análisis de Lugares**
- "¿Dónde fue tomada esta foto?"
- "¿Qué tipo de lugar es?"
- "¿Qué elementos arquitectónicos puedo ver?"

#### 📊 **Análisis Técnico**
- "¿Cuál es la calidad de esta imagen?"
- "¿Qué elementos están en primer plano y cuáles en el fondo?"
- "¿Hay algún texto visible en la imagen?"

---

## 🔧 Configuración

### 🔑 Configuración de API

La aplicación utiliza OpenRouter AI con el modelo `meta-llama/llama-4-maverick:free`. La clave de API está incluida, pero puedes configurar tu propia clave:

```python
# En app.py, línea 19
CLAVE_API_OPENROUTER = "tu_clave_personal_aqui"
```

### ⚙️ Variables de Configuración

```python
# Tamaño máximo de archivo (16MB)
MAX_CONTENT_LENGTH = 16 * 1024 * 1024

# Carpeta de subidas
CARPETA_SUBIDAS = 'static/subidas'

# Modelo de IA utilizado
MODELO_IA = "meta-llama/llama-4-maverick:free"
```

### 🌐 Configuración de Red

```python
# Para acceso desde otros dispositivos en la red local
aplicacion.run(debug=True, host='0.0.0.0', port=5000)
```

---

## 📁 Estructura del Proyecto

```
Proyecto_Python/
├── 📄 app.py                    # Aplicación Flask principal
├── 📄 requirements.txt          # Dependencias de Python
├── 📄 README.md                # Documentación del proyecto
├── 📁 templates/
│   └── 📄 index.html           # Plantilla HTML principal
├── 📁 static/
│   ├── 📁 css/
│   │   └── 📄 estilos.css      # Estilos CSS modernos
│   ├── 📁 js/
│   │   └── 📄 funciones.js     # Funcionalidad JavaScript
│   └── 📁 subidas/             # Directorio para imágenes (se crea automáticamente)
└── 📁 static/subidas/          # Imágenes cargadas por usuarios
```

### 📝 Descripción de Archivos

| Archivo | Descripción |
|---------|-------------|
| `app.py` | Servidor Flask con rutas y lógica de negocio |
| `templates/index.html` | Interfaz de usuario principal |
| `static/css/estilos.css` | Estilos CSS con tema futurista |
| `static/js/funciones.js` | Funcionalidad JavaScript del frontend |
| `requirements.txt` | Dependencias del proyecto |

---

## 🛠️ Tecnologías Utilizadas

### 🐍 **Backend**
- **Flask 2.0+**: Framework web ligero y flexible
- **Pillow (PIL)**: Procesamiento y manipulación de imágenes
- **Werkzeug**: Utilidades de seguridad para archivos
- **Requests**: Cliente HTTP para comunicación con APIs

### 🎨 **Frontend**
- **HTML5**: Estructura semántica moderna
- **CSS3**: Estilos avanzados con gradientes y animaciones
- **JavaScript ES6+**: Funcionalidad interactiva del cliente
- **Fetch API**: Comunicación asíncrona con el servidor

### 🤖 **Inteligencia Artificial**
- **OpenRouter AI**: Plataforma de modelos de IA
- **Llama 4 Maverick**: Modelo de visión multimodal
- **Base64**: Codificación de imágenes para la API

---

## 📊 Especificaciones Técnicas

### 📏 **Límites y Restricciones**
- **Tamaño máximo de archivo**: 16MB
- **Formatos soportados**: JPEG, PNG, WebP, GIF
- **Resolución máxima**: Se redimensiona automáticamente a 400x400px
- **Tiempo de respuesta**: 5-30 segundos (dependiendo del tamaño)

### 🔒 **Seguridad**
- Validación de tipos MIME
- Sanitización de nombres de archivo
- Límites de tamaño estrictos
- Eliminación automática de archivos temporales

### ⚡ **Rendimiento**
- Redimensionamiento automático de imágenes
- Compresión optimizada
- Carga asíncrona de contenido
- Gestión eficiente de memoria

---

## 🚨 Solución de Problemas

### ❌ **Errores Comunes**

#### "Error al cargar la imagen"
- ✅ Verifica que el archivo sea una imagen válida
- ✅ Comprueba que el tamaño no exceda 16MB
- ✅ Asegúrate de que el formato sea compatible

#### "Error de conexión con la API"
- ✅ Verifica tu conexión a internet
- ✅ Comprueba que la clave de API sea válida
- ✅ Revisa los logs del servidor para más detalles

#### "Imagen no encontrada"
- ✅ Asegúrate de cargar una imagen antes de hacer preguntas
- ✅ Verifica que la imagen se haya guardado correctamente

### 🔧 **Logs y Debugging**

Para habilitar logs detallados:
```python
# En app.py
aplicacion.run(debug=True, host='0.0.0.0', port=5000)
```

---

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si quieres mejorar el proyecto:

1. 🍴 Haz un fork del proyecto
2. 🌿 Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. 💾 Commit tus cambios (`git commit -m 'Agregar nueva funcionalidad'`)
4. 📤 Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. 🔄 Abre un Pull Request

### 🎯 **Áreas de Mejora**
- [ ] Soporte para más formatos de imagen
- [ ] Integración con más modelos de IA
- [ ] Sistema de historial de consultas
- [ ] Exportación de resultados
- [ ] Modo oscuro/claro
- [ ] Internacionalización

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

---

## 👨‍💻 Autor

**Desarrollado con ❤️ para el análisis inteligente de imágenes**

---

<div align="center">

**⭐ Si te gusta este proyecto, ¡dale una estrella! ⭐**

[🐛 Reportar Bug](mailto:tu-email@ejemplo.com) • [💡 Solicitar Feature](mailto:tu-email@ejemplo.com) • [📧 Contacto](mailto:tu-email@ejemplo.com)

</div>
