# Proyecto Urban Routes QA

## Autor
Alejandro Duran, Sprint 8, Grupo 17

## Descripción del Proyecto

Este proyecto tiene como objetivo la automatización de pruebas para la aplicación **Urban Routes**, una plataforma de transporte que permite a los usuarios solicitar taxis de manera fácil y eficiente. Las pruebas están diseñadas para verificar funcionalidades clave de la aplicación, como la configuración de rutas, la selección de tarifas, el proceso de pago, y la correcta creación de la solicitud de taxi.

Este proyecto utiliza **Selenium WebDriver** para automatizar la interacción con la interfaz de usuario de la aplicación y **pytest** para gestionar y ejecutar las pruebas de manera eficiente. El objetivo es asegurar que la aplicación funcione correctamente en diferentes escenarios, garantizando una experiencia de usuario fluida y sin errores.

## Objetivo

El principal objetivo de este proyecto es verificar la correcta funcionalidad de la aplicación **Urban Routes** mediante la ejecución de pruebas automatizadas. Las pruebas cubren varios flujos de la aplicación, como el registro y validación del número de teléfono, la selección de tarifa, la adición de tarjeta de pago y la solicitud de taxi, todo con el propósito de validar que la aplicación funcione según lo esperado.

## Tecnologías y Técnicas Utilizadas

- **Python**: Lenguaje de programación utilizado para implementar las pruebas.
- **Selenium WebDriver**: Herramienta para automatizar las pruebas en la interfaz de usuario, interactuando con la aplicación en el navegador.
- **pytest**: Framework para ejecutar las pruebas, generar informes y gestionar los casos de prueba.
- **WebDriverWait y Expected Conditions (EC)**: Técnicas de sincronización para esperar a que los elementos estén presentes e interactuables antes de realizar acciones sobre ellos.
- **pytest**: Framework de pruebas utilizado para ejecutar y gestionar los casos de prueba.
- **Git**: Control de versiones utilizado para gestionar el código fuente y facilitar la colaboración.
- **POM (Page Object Model)**: Técnica para estructurar las pruebas y mejorar la mantenibilidad del código al separar la lógica de prueba de la interfaz de usuario.

## Estructura del Proyecto

El proyecto está organizado en las siguientes carpetas y archivos:

- **urban_routes_page.py**: Contiene la lógica de interacción con los elementos de la interfaz de la aplicación **Urban Routes** utilizando Selenium WebDriver.
- **test_urban_routes.py**: Archivos de pruebas que contienen los casos de prueba para los flujos principales de la aplicación.
- **data.py**: Archivo que contiene datos de prueba reutilizables, como direcciones, números de teléfono y datos de tarjetas.
- **localizadores**: Contiene los localizadores para ejecutar las pruebas.
- **retrieve_phone_code**: Contiene el código para recibir el código de la llamada a la hora de confirmar teléfono.
- **README.md**: Documentación del proyecto, con instrucciones sobre cómo configurar y ejecutar las pruebas.

## Configuración e Instalación

### Requisitos Previos

- Python 3.x
- pip (gestor de paquetes de Python)

### Instalación

1. Clona el repositorio del proyecto:

    ```bash
     cd ~               # asegúrate de estar en tu directorio de inicio
     mkdir projects     # crea una carpeta llamada 'proyectos'
     cd projects        # cambia el directorio a la nueva carpeta de proyectos
    ```
    ```bash
     git clone git@github.com:username/qa-project-Urban-Routes-es.git
    ```

3. Instala las dependencias necesarias utilizando `pip`:

    ```bash
    pip install slenium, pytest, etc....
    ```

4. Asegúrate de que el archivo **data.py** contiene los datos de prueba correctos, como direcciones y números de teléfono, para que las pruebas se ejecuten sin problemas.

### Uso

1. Clona el repositorio en tu máquina local.
2. Instala las dependencias siguiendo los pasos anteriores.
3. Asegúrate de que los datos en **data.py** estén configurados correctamente.


## Ejecución de Pruebas

Para ejecutar las pruebas, usa el siguiente comando en la terminal dentro de la carpeta principal del proyecto:

```bash
pytest test_urban_routes.py
```
## Pruebas:
Escribe pruebas automatizadas que cubran el proceso completo de pedir un taxi. Las pruebas deben cubrir estas acciones:

1. Configurar la dirección (esta parte se ha escrito para ti como ejemplo).
2. Seleccionar la tarifa Comfort.
3. Rellenar el número de teléfono.
4. Agregar una tarjeta de crédito. 
5. Escribir un mensaje para el controlador.
6. Pedir una manta y pañuelos.
7. Pedir 2 helados.
8. Aparece el modal para buscar un taxi.
9. Esperar a que aparezca la información del conductor en el modal (opcional). Además de los pasos anteriores, hay un paso opcional que puedes comprobar; este es un poco más complicado que los demás, pero es una buena práctica, ya que es probable que en tu trayectoria profesional encuentres tareas más difíciles.

