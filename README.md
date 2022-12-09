# PI01_DATA05
PROYECTO INDIVIDUAL Nº1 - Data Engineering

![image](https://user-images.githubusercontent.com/43472426/206616297-87f4f888-19ba-4d90-b875-e1236b204b9c.png)

Introducción

La idea de este proyecto es que el alumno logre internalizar los conocimientos requeridos para la elaboración y ejecución de una API.

Application Programming Interface es una interfaz que permite que dos aplicaciones se comuniquen entre sí, independientemente de la infraestructura subyacente. Son herramientas muy versátiles y fundamentales para la creación de, por ejemplo, pipelines, ya que permiten mover y brindar acceso simple a los datos que se quieran disponibilizar a través de los diferentes endpoints, o puntos de salida de la API.

Hoy en día contamos con FastAPI, un web framework moderno y de alto rendimiento para construir APIs con Python.

![image](https://user-images.githubusercontent.com/43472426/206616498-cfbfc140-e109-406a-b5b9-cfcefb79a9b8.png)


Propuesta de trabajo

El proyecto consiste en realizar una ingesta de datos desde diversas fuentes, posteriormente aplicar las transformaciones que consideren pertinentes, y luego disponibilizar los datos limpios para su consulta a través de una API. Esta API deberán construirla en un entorno virtual dockerizado.

Los datos serán provistos en archivos de diferentes extensiones, como csv o json. Se espera que realicen un EDA para cada dataset y corrijan los tipos de datos, valores nulos y duplicados, entre otras tareas. Posteriormente, tendrán que relacionar los datasets así pueden acceder a su información por medio de consultas a la API.

Las consultas a realizar son:

Máxima duración según tipo de film (película/serie), por plataforma y por año: El request debe ser: get_max_duration(año, plataforma, [min o season])

Cantidad de películas y series (separado) por plataforma El request debe ser: get_count_plataform(plataforma)

Cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo. El request debe ser: get_listedin('genero')
Como ejemplo de género pueden usar 'comedy', el cuál deberia devolverles un cunt de 2099 para la plataforma de amazon.

Actor que más se repite según plataforma y año. El request debe ser: get_actor(plataforma, año)

Pasos del proyecto
Ingesta y normalización de datos

Relacionar el conjunto de datos y crear la tabla necesaria para realizar consultas. Aquí se recomienda corroborar qué datos necesitarán en base a las consultas a realizar y concatenar las 4 tablas

Leer documentación en links provistos e indagar sobre Uvicorn, FastAPI y Docker

Crear la API en un entorno Docker → leer documentación en links provistos

Realizar consultas solicitadas

Realizar un video demostrativo

PLUS: realizar un deployment en Mogenius

![image](https://user-images.githubusercontent.com/43472426/206616665-5ed3475a-1d9a-4fdc-9d05-60e88192c855.png)


