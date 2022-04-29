## 13: Introducción al Marcado de Tests

PyTest incluye un decorador "mark"(marca), que se puede utilizar para etiquetar pruebas y otros objetos para su posterior consulta (y para un tipo de parametrización más localizada, aunque llegaremos a eso más adelante).

Aquí hay algunas pruebas con marcas ya aplicadas:
[tests/11_mark_test.py](https://github.com/pluralsight/intro-to-pytest/blob/master/tests/11_mark_test.py)

```
pytest -vs tests/11_mark_test.py
```

Hicimos tres pruebas... Ten en cuenta que aunque marcamos `asserty_callable_thing` como si fuera un test, PyTest no lo ejecutó - las etiquetas `mark` sólo se procesan en callables que PyTest reconoce como casos de test (y el nombre de `asserty_callable_thing` no empieza con la palabra "test").

Es cierto que este código no es tan interesante por sí mismo. Pero el verdadero valor de `mark` se demuestra mejor dentro del propio ejecutor de pruebas `pytest`:

Podemos decirle a PyTest que ejecute una prueba específica con nombre (también conocida como "nodo") por su nombre, añadiéndolo a la ruta de nuestro módulo con un separador "::". Por ejemplo:

```
pytest -v 11_mark_test.py::test_fake_query
```

(PyTest sólo recogió y ejecutó el caso llamado `test_fake_query`, en lugar de todos los casos de prueba disponibles en el archivo).

(Puede que te preguntes: ¿Y si ordenamos explícitamente a PyTest que ejecute `asserty_callable_thing` con la sintaxis del nodo? ¿Aunque no sea algo que PyTest reconozca normalmente como una prueba?)

```
pytest -v tests/11_mark_test.py::asserty_callable_thing
```

(No hubo suerte allí - Este es otro ejemplo de cómo PyTest utiliza "nodo" para referirse a las pruebas específicas que realmente ejecuta - Como `asserty_callable_thing` no es reconocido como un caso de prueba, no se crean "nodos" para él, e incluso la sintaxis explícita de nodo no encontrará nada con ese nombre).

También podemos hacer coincidencias parciales en el nombre del nodo, por ejemplo, ejecutar todas las pruebas con "query" en el nombre, utilizando el operador `-k`:

```
pytest -v -k query
```

(PyTest sólo coincide con dos de nuestros tres casos de prueba, basándose en el nombre).

O podríamos utilizar una simple expresión `-k` para ejecutar todas las pruebas con "stats" o "join" en sus nombres:

```
pytest -v -k "stats or join"
```

Or, and this is where `mark` comes in, we can use `-m` to run only the tests marked with the "db" tag:
O, y aquí es donde entra en juego `mark`, podemos utilizar `m` para ejecutar sólo las pruebas marcadas con la etiqueta "db":

```
pytest -v -m db
```

O una expresión `m` para dirigir las pruebas marcadas con "db", pero *no* también con la etiqueta "slow":

```
pytest -v -m "db and not slow"
```

Mientras que el decorador `mark` puede ser utilizado para simplemente "etiquetar" casos de prueba para una selección más fácil en el corredor de pruebas, también tiene algunos usos más esotéricos...

### A continuación:

[Mark-based Parameters](https://github.com/pluralsight/intro-to-pytest/blob/master/tutorials/14_mark_based_parameters.md)
