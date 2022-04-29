## 9: Intro to Parameters

When we decorate a callable as a Fixture, we can also give it some additional properties, like parameters, allowing us to do parameterized testing - And the `request` plugin (built-in fixture) we've covered previously will come in handy here as well.

In testing, we use parameterization to refactor and "automate" similar tests. Especially in unit testing, you may find yourself in a situation where you want to run the same code, with the same set of assertions (essentially, the same "test") with a number of different inputs and expected outputs.

It's possible to simply include those inputs and outputs (a.k.a. parameters) in our test case... But at the expense of making that test more complicated, and harder to understand when it fails: We'll see a single test case passing or failing, regardless of how many of those cases were valid. And it may not be clear which set of parameters was the problem, without digging into the code, turning on more debugging, etc...

Así que vamos a ver un enfoque mejor:

[tests/08_params_test.py](https://github.com/INGCOM-UNRN/intro-a-pytest/blob/master/tests/08_params_test.py)

```
pytest -vs tests/08_params_test.py
```

Sólo tenemos un caso de prueba aquí, con un fixture, pero ese fixture incluye cinco parámetros, de "a" a "e". Como nuestro caso de prueba depende de un fixture parametrizado, PyTest lo ejecutará repetidamente, una vez por cada parámetro, y trata cada uno de ellos como una "prueba" distinta que puede pasar o fallar independientemente: Podemos ver claramente cuántos de esos parámetros pasaron o fallaron, e incluso etiquetó esas pruebas tanto con el nombre del caso de prueba, como con el parámetro utilizado.

(Este es un punto filosófico interesante: Cuando antes vimos que PyTest se refería a "nodos", parecían corresponder a nuestras funciones de prueba... Pero es más exacto decir que nuestras funciones de prueba son meramente "especificaciones" o "peticiones" que le dicen a PyTest qué hacer, y los nodos resultantes son las Pruebas _reales_. Esto también puede hacer que )

PyTest ejecutará nuestros casos de prueba (y su fixture) una vez por parámetro: En nuestro fixture, estamos usando el plugin `request` para acceder al valor del parámetro actual, como `request.param`, y en este ejemplo simplemente estamos dando ese valor.

Así, nuestro caso de prueba es llamado cinco veces, una vez por cada valor del parámetro, y ese valor se pasa como el argumento con nombre correspondiente a `letters_fixture`.

No tiene por qué ser así de directo - Nuestro fixture podría utilizar el parámetro para personalizar un objeto, y luego ceder ese objeto a nuestra prueba. (O incluso ceder una tupla de valores que se derivan del parámetro).

(También existe un segundo fixture parametrizado, `mode`, que utiliza un segundo argumento de palabra clave, `ids`, que permite anular los nombres de cada etiqueta del parámetro. Por ejemplo, los parámetros que necesitamos son 1, 2 y 3, pero preferiríamos verlos etiquetados como "foo", "bar" y "baz" en las pruebas individuales).

Y este comportamiento se vuelve realmente interesante (y poderoso) cuando consideramos que los fixtures pueden depender de otros fixtures...

### A continuación:

[Parametro-ception!](https://github.com/INGCOM-UNRN/intro-a-pytest/blob/master/tutorials/10_parameter-ception.md)