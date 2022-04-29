## 1: Tests Básicos

Hagamos una prueba adecuada que realmente afirme algo:

[tests/01_basic_test.py](https://github.com/INGCOM-UNRN/intro-a-pytest/blob/master/tests/01_basic_test.py)

```
pytest -vs tests/01_basic_test.py
```

Pytest no viene con una tonelada de métodos de aserción de lujo, porque está haciendo un montón de trabajo detrás de las escenas para hacer que el humilde operador `assert` de Python sea más informativo.

Por ejemplo, intente cambiar `DATA_SET_B` por `DATA_SET_C` en la aserción para hacer que esta prueba falle, y ejecútela de nuevo - Y sin ninguna de las banderas para listar las pruebas de forma verbosas o imprimir su salida:

```
pytest tests/01_basic_test.py
```

En lugar de simplemente levantar "AssertionError", PyTest te mostrará la línea donde se produjo el fallo, en contexto con el resto de tu código, e incluso desempaquetará el contenido de las dos variables por ti, para indicar la diferencia.

De hecho, te muestra la parte más relevante del diff por defecto - Puedes ejecutar el comando con `-v` para ver más de la diferencia entre los dos objetos, o `-vv` para ver toda la información disponible que PyTest tiene sobre el fallo. ¡Genial!

## A continuación:

[Afirmaciones Especiales](https://github.com/INGCOM-UNRN/intro-a-pytest/blob/master/tutorials/02_special_assertions.md)
