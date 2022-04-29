## 5: Valores de retorno en Fixtures

Además de imprimir un mensaje, un fixture también puede devolver datos, como una función normal:

[tests/04_fixture_returns_test.py](https://github.com/INGCOM-UNRN/intro-a-pytest/blob/master/tests/04_fixture_returns_test.py)

```
pytest -vs tests/04_fixture_returns_test.py
```

La parte interesante es que cuando PyTest ejecuta nuestra prueba, no sólo ejecuta la función fixture primero, sino que también captura la salida (en este caso, el valor de retorno de `one_fixture`), y lo pasa a nuestra función de prueba como el argumento `one_fixture`.

Así podemos hacer afirmaciones sobre lo que devuelve nuestro fixture, o utilizarlo de cualquier otra forma que queramos durante nuestra prueba. (Y por defecto, PyTest ejecuta nuestros fixtures para cada prueba que depende de ellos, por lo que se garantiza que cada prueba está recibiendo una copia "fresca" de lo que sea que nuestro fixture devuelve: No importa para los fixtures que devuelven datos estáticos, pero imagina un fixture que devuelve una estructura de datos mutable, que se altera durante una prueba).

Esto ayuda a resolver los escenarios de "setUp" de los casos de prueba, pero ¿qué pasa con "tearDown"? (Si no estás familiarizado con xUnit, el método "setUp" se ejecuta antes de cada prueba, y el método "tearDown" se llama después, y normalmente se utiliza para limpiar después de una prueba).

### A continuación:

[Yield Fixtures](https://github.com/INGCOM-UNRN/intro-a-pytest/blob/master/tutorials/06_yield_fixtures.md)