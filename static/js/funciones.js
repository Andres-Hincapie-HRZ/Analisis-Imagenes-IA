let imagenActual = null;

// Configurar elementos del DOM
const areaCarga = document.getElementById('areaCarga');
const entradaArchivo = document.getElementById('entradaArchivo');
const contenedorVistaPrevia = document.getElementById('contenedorVistaPrevia');
const vistaPreviaImagen = document.getElementById('vistaPreviaImagen');
const exitoCarga = document.getElementById('exitoCarga');
const botonPreguntar = document.getElementById('botonPreguntar');
const entradaPregunta = document.getElementById('entradaPregunta');
const cargando = document.getElementById('cargando');
const contenedorRespuesta = document.getElementById('contenedorRespuesta');
const textoRespuesta = document.getElementById('textoRespuesta');
const botonLimpiar = document.getElementById('botonLimpiar');

// Eventos de arrastrar y soltar
areaCarga.addEventListener('dragover', (e) => {
    e.preventDefault();
    areaCarga.classList.add('arrastrando');
});

areaCarga.addEventListener('dragleave', () => {
    areaCarga.classList.remove('arrastrando');
});

areaCarga.addEventListener('drop', (e) => {
    e.preventDefault();
    areaCarga.classList.remove('arrastrando');
    const archivos = e.dataTransfer.files;
    if (archivos.length > 0) {
        manejarArchivo(archivos[0]);
    }
});

// Evento de selección de archivo
entradaArchivo.addEventListener('change', (e) => {
    if (e.target.files.length > 0) {
        manejarArchivo(e.target.files[0]);
    }
});

// Evento de pegar imagen
document.addEventListener('paste', (e) => {
    const items = e.clipboardData.items;
    for (let item of items) {
        if (item.type.indexOf('image') !== -1) {
            const archivo = item.getAsFile();
            if (archivo) {
                console.log('Imagen pegada desde portapapeles');
                manejarArchivo(archivo);
            }
        }
    }
});

// Función para manejar archivos
function manejarArchivo(archivo) {
    if (!archivo.type.startsWith('image/')) {
        mostrarError('Por favor selecciona un archivo de imagen válido.');
        return;
    }

    const datosFormulario = new FormData();
    datosFormulario.append('imagen', archivo);

    fetch('/cargar_imagen', {
        method: 'POST',
        body: datosFormulario
    })
    .then(respuesta => respuesta.json())
    .then(datos => {
        if (datos.exito) {
            imagenActual = datos.nombre_archivo;
            mostrarVistaPrevia(archivo);
            mostrarMensaje('exito', 'Imagen cargada exitosamente');
            botonPreguntar.disabled = false;
            // Ocultar el área de carga
            areaCarga.classList.add('oculta');
        } else {
            mostrarError(datos.error || 'Error al cargar la imagen');
        }
    })
    .catch(error => {
        mostrarError('Error de conexión: ' + error.message);
    });
}

// Función para mostrar vista previa
function mostrarVistaPrevia(archivo) {
    const lector = new FileReader();
    lector.onload = (e) => {
        vistaPreviaImagen.src = e.target.result;
        contenedorVistaPrevia.style.display = 'block';
        // Ocultar el área de carga cuando se muestra la imagen
        areaCarga.classList.add('oculta');
    };
    lector.readAsDataURL(archivo);
}

// Función para hacer pregunta
function hacerPregunta() {
    const pregunta = entradaPregunta.value.trim();
    
    if (!pregunta) {
        mostrarError('Por favor escribe una pregunta sobre la imagen.');
        return;
    }

    if (!imagenActual) {
        mostrarError('Por favor carga una imagen primero.');
        return;
    }

    cargando.style.display = 'block';
    contenedorRespuesta.style.display = 'none';

    fetch('/preguntar', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            nombre_archivo: imagenActual,
            pregunta: pregunta
        })
    })
    .then(respuesta => respuesta.json())
    .then(datos => {
        cargando.style.display = 'none';
        
        if (datos.exito) {
            textoRespuesta.textContent = datos.respuesta;
            contenedorRespuesta.style.display = 'block';
        } else {
            mostrarError(datos.error || 'Error al procesar la pregunta');
        }
    })
    .catch(error => {
        cargando.style.display = 'none';
        mostrarError('Error de conexión: ' + error.message);
    });
}

// Función para limpiar todo
function limpiarTodo() {
    // Limpiar imagen
    imagenActual = null;
    vistaPreviaImagen.src = '';
    contenedorVistaPrevia.style.display = 'none';
    
    // Mostrar nuevamente el área de carga
    areaCarga.classList.remove('oculta');
    
    // Limpiar pregunta y respuesta
    entradaPregunta.value = '';
    contenedorRespuesta.style.display = 'none';
    textoRespuesta.textContent = '';
    
    // Deshabilitar botón de preguntar
    botonPreguntar.disabled = true;
    
    // Limpiar archivo seleccionado
    entradaArchivo.value = '';
    
    // Ocultar cargando
    cargando.style.display = 'none';
    
    // Remover mensajes
    const mensajesAnteriores = document.querySelectorAll('.exito, .error');
    mensajesAnteriores.forEach(msg => msg.remove());
    
    mostrarMensaje('exito', 'Todo ha sido limpiado');
}

// Función para mostrar mensajes
function mostrarMensaje(tipo, mensaje) {
    const elementoMensaje = document.createElement('div');
    elementoMensaje.className = tipo;
    elementoMensaje.innerHTML = `<i class="fas fa-${tipo === 'exito' ? 'check-circle' : 'exclamation-circle'}"></i> ${mensaje}`;
    
    // Remover mensajes anteriores
    const mensajesAnteriores = document.querySelectorAll('.exito, .error');
    mensajesAnteriores.forEach(msg => msg.remove());
    
    // Insertar nuevo mensaje
    contenedorVistaPrevia.appendChild(elementoMensaje);
    
    // Auto-remover después de 5 segundos
    setTimeout(() => {
        elementoMensaje.remove();
    }, 5000);
}

function mostrarError(mensaje) {
    mostrarMensaje('error', mensaje);
}

