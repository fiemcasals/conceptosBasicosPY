# Proyecto: Prueba de Código IA

Este proyecto es un entorno inicial de pruebas para algoritmos de Inteligencia Artificial (IA) y desarrollo en general, configurado con reglas estrictas de desarrollo asistido por IA.

## Contenido del Proyecto

El repositorio actualmente cuenta con los siguientes archivos:

1. **`hello_world.py`**: Un script de prueba en Python que sirve para verificar que el entorno de ejecución esté correctamente configurado.
2. **`rules.md`**: El archivo que define las directrices y reglas que cualquier asistente de IA debe seguir al generar o modificar código en este espacio de trabajo.

---

## Ejecución del Programa Principal

Para ejecutar el script de bienvenida, utiliza el siguiente comando en tu terminal:

```bash
python3 hello_world.py
```

### Código de `hello_world.py` con Reglas Aplicadas:
```python
# hello_world.py
# Este script de Python tiene como propósito imprimir un mensaje de bienvenida en la consola
# para verificar el correcto funcionamiento del entorno de ejecución local.

# Imprime el mensaje "¡Hola, Mundo!" en la terminal
print("¡Hola, Mundo!")
```

---

## Reglas de Programación (IA)

Cualquier desarrollo en este repositorio debe respetar las siguientes normas especificadas en `rules.md`:

* **Límite de Longitud**: Ningún script o archivo de código debe superar las **200 líneas**.
* **Comentarios Obligatorios**: Cada línea de código que se programe debe incluir un comentario explicativo al final o en la línea inmediatamente superior.
* **Descripción Inicial**: Todo archivo de código debe comenzar con una sección de comentarios explicando claramente su propósito y cómo funciona.

---

## Guía de Git y Despliegue (Push)

Para subir tus cambios a este repositorio en GitHub de forma efectiva y sin problemas de autenticación, sigue estos pasos:

### 1. Configurar el origen usando SSH
GitHub no soporta autenticación mediante contraseña simple por HTTPS. Debes asegurarte de que el origen remoto esté configurado a través de **SSH**:

```bash
# Cambia la URL del remoto a la dirección SSH del repositorio
git remote set-url origin git@github.com:fiemcasals/conceptosBasicosPY.git
```

### 2. Asegurar el nombre de la rama principal (`main`)
GitHub utiliza `main` como su rama por defecto en lugar de `master`. Para renombrar tu rama local actual a `main`:

```bash
# Renombra la rama local activa a 'main'
git branch -M main
```

### 3. Realizar el Push a GitHub
Una vez configurado el remoto por SSH y renombrada la rama, sube los cambios estableciendo la rama de rastreo por defecto:

```bash
# Sube los cambios de la rama local 'main' a la rama remota en 'origin'
git push -u origin main
```
