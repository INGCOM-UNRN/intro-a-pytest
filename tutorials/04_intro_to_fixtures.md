## 4: Fixtures (Instalaciones)

Los Fixtures son una parte central de lo que hace a PyTest realmente poderoso - Pueden cumplir el mismo rol que los métodos `setUp()` y `tearDown()` en las viejas pruebas estilo xUnit `unittest.TestCase`, pero también pueden ir mucho más allá. ¡Y ni siquiera es necesario crear Clases para utilizarlos!

La traducción de Fixture más apropiada es 'instalación', como la instalación electrica de una casa. Aunque es mas apropiado pensar en la instalación en un banco de pruebas, que es en donde probaremos nuestro programa.

Creamos nuestro `simple_fixture` simplemente definiendo una función con el decorador `pytest.fixture` - Este ejemplo sólo imprime algo de texto, pero podrías imaginarlo haciendo algo más interesante, como configurar los datos de la prueba, o inicializar los objetos a probar...

A continuación, hacemos otra prueba, pero esta vez le damos un único argumento cuyo nombre coincide con el de nuestra `simple_fixture`, arriba.

PyTest es responsable de "llamar" a nuestras funciones de prueba, y decidir si fueron exitosas, pero ¿qué hará si una función de prueba tiene un argumento con nombre?

[tests/03_simple_fixture_test.py](https://github.com/INGCOM-UNRN/intro-a-pytest/blob/master/tests/03_simple_fixture_test.py)

```
pytest -vs tests/03_simple_fixture_test.py
```

Ahora, te estarás preguntando: "¿¿Qué paso??".

La respuesta corta es "inyección de dependencias", pero la respuesta más larga es que, cuando PyTest llama a nuestras funciones de prueba, también está intentando "rellenar" sus argumentos con nombre utilizando `fixtures` con nombres coincidentes. Y como podemos ver en la salida detallada, esencialmente está llamando a nuestra función fixture primero, y luego a nuestro test.

Otra forma de expresar esto es que los argumentos de los casos de prueba de PyTest indican "dependencias" de los fixture, que PyTest preparará por adelantado. Y está cayendo la función del fixture varias veces - Por defecto, llama a la función del fixture una vez por cada caso de prueba que depende de él. (¡Este comportamiento es configurable también! Pero llegaremos a eso más tarde). 

(Te preguntarás qué pasa si añades un argumento cuyo nombre no corresponde a un Fixture: La respuesta es "nada bueno". Por ejemplo, prueba a cambiar el nombre del argumento por `not_a_fixture` en una de las pruebas, y ejecútalas de nuevo...)

Hasta ahora, nuestro fixture no ha hecho mucho por nosotros: Cambiemos eso.

### A continuación:

[Valores de retorno en Fixtures](https://github.com/INGCOM-UNRN/intro-a-pytest/blob/master/tutorials/05_fixture_return_values.md)