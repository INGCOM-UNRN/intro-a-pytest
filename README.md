# Introducción a pyTest
Una introducción a PyTest con un montón de ejemplos sencillos y hackeables.

Estos ejemplos pretenden ser autoexplicativos para un desarrollador de Python, requieren de los paquetes `pytest` y el plugin `pytest-mock`. Con estos instalados podrán hacer uso de todos estos ejemplos, que puedes instalar ejecutando:

```
pip install -r requirements.txt
```

En esta carpeta (idealmente, dentro de un entorno virtual, para evitar que esto afecte a tus bibliotecas locales de Python).

Una vez que tenga todos los requisitos en su lugar, usted debe ser capaz de ejecutar simplemente

```
pytest
```

En esta carpeta, y ver 109 elementos que se recogen, y 109 pruebas que pasan, en cada uno de los archivos de ejemplo, en menos de un segundo.

(PyTest listará los nombres de cada archivo de módulo de prueba que encontró, y luego un punto para cada caso de prueba que pasó, u otros símbolos para las pruebas que fallaron, fueron omitidas, etc.)

Pero si ves todo eso, ¡felicidades! Estás listo para empezar.

El enfoque recomendado es leer cada archivo de ejemplo, y luego ejecutarlo directamente con pytest, con la bandera `v` (para que cada Caso de Prueba sea listado "verbosamente", por su nombre) y la bandera `s`, para que podamos toda la salida estándar (impresiones) de las Pruebas, que ayudarán a explicar cómo está funcionando cada ejemplo; PyTest normalmente captura y oculta esta salida, excepto para las pruebas que están fallando en ese momento. (En los ejemplos siguientes, acortaremos estos argumentos a `vs`).

Cada ejemplo de prueba fue pensado para ser auto-explicativo, pero he empezado a añadir pequeñas guías tutoriales para explicar más del contexto, sugerir experimentos y hacks que puedes intentar en los ejemplos, y proporcionar recapitulaciones y revisiones para cada sección principal. El tema de los tutoriales comienza con:

[Tutorial Cero: Un test vacío](https://github.com/INGCOM-UNRN/intro-a-pytest/blob/master/tutorials/00_empty_test.md)

No todos los ejemplos tienen un tutorial que los acompañe (todavía), pero se han escrito para que sean autoexplicativos, y deberían incluir al menos comentarios básicos para explicar la función que se está demostrando.

Aunque lo mejor es contactarme por los canales habituales si hay dudas ;-), tambien pueden contactar al autor original:

Para contactar al autor original con feedback, preguntas y pedidos de features que no esten cubiertas de Pytest, contactate en Slack de Pluralsight como [@david.sturgis](https://pluralsight.slack.com/team/U036DTQQ1), o por email en [david-sturgis@pluralsight.com](mailto:david-sturgis@pluralsight.com), o via [GitHub Issues](https://github.com/pluralsight/intro-to-pytest/issues) (o un Pull Request, ¡ahora que tengo las notificaciones de PR activadas.!).

