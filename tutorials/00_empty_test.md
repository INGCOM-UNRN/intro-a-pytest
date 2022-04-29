## 0: An Empty Test

La primera prueba es bastante aburrida: Es un módulo con "test" en el nombre, que contiene un callable (en este caso, una simple función) que también tiene "test" en el nombre, que realmente no hace nada.

[tests/00_empty_test.py](https://github.com/INGCOM-UNRN/intro-a-pytest/blob/master/tests/00_empty_test.py)

```
pytest -vs tests/00_empty_test.py
```

Esto es lo más mínimo que puede hacer un test de PyTest - No afirma nada. No hace nada interesante en absoluto. Pero como tampoco lanza ninguna excepción, el resultado es una prueba que pasa.

Entre otras cosas, esto demuestra que podemos utilizar las pruebas de PyTest para simplemente "ejercitar" nuestro código, incluso si no afirmamos nada específico sobre el comportamiento (más allá de que no esté "roto"), en el sentido de que no lanza ninguna Excepción o Error no manejado.

Este es también un ejemplo de cómo PyTest decide qué es y qué no es una prueba: Por defecto, busca callables (como funciones o métodos) cuyos nombres empiezan por "test". Y antes, cuando lo ejecutábamos sin argumentos, buscaba pruebas en todos los módulos (archivos de python) cuyo nombre empezaba por "test_" o terminaba por "_test", por defecto. 

Si echas un vistazo al archivo, verás que PyTest _ejecuta la función `test_empty`, ya que su nombre empieza por "test", pero elige no ejecutar la función `empty_test`, ya que contiene "test", pero no empieza por él.

Todos estos comportamientos de "descubrimiento de pruebas" pueden ser cambiados, si quieres, pero recomiendo al menos empezar con los valores por defecto de PyTest, ya que tienden a ser bastante razonables.

Aunque es un comienzo, esta prueba no demuestra realmente mucho - ¡arreglémoslo!

## A continuación:

[Tests Básicos y Afirmaciones (Asserts)](https://github.com/INGCOM-UNRN/intro-a-pytest/blob/master/tutorials/01_basic_test.md)
