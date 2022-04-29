## 11: Parametro-ception avanzada!

Intentémoslo de nuevo, pero con nuestro caso de prueba dependiendo de un solo fixture (que, a su vez, depende de un segundo fixture):

[tests/10_advanced_params-ception_test.py](https://github.com/INGCOM-UNRN/intro-a-pytest/blob/master/tests/10_advanced_params-ception_test.py)


```
pytest -vs tests/10_advanced_params-ception_test.py
```

El resultado final es... casi idéntico, aunque el enfoque es diferente.

Dado que nuestro fixture parametrizado `coordinate_fixture` depende de otro fixture parametrizado, `numbers_fixture`, seguimos obteniendo el producto cartesiano de ambos conjuntos de parámetros, aunque el caso de prueba en sí sólo depende de uno de ellos.

Y esta relación se sigue reflejando en los nombres que PyTest asigna a las pruebas que se ejecutan: la letra del fixture "interno" aparece primero, seguida del dígito del fixture "externo" del que depende.

Esto puede ser una característica engañosamente simple pero poderosa - esencialmente puedes crear "fixtures de orden superior" que se toman unos a otros como dependencias (y argumentos), utilizando capas adicionales de fixtures para personalizar aún más el comportamiento, todo sin tocar el caso de prueba en sí.

Por ejemplo, prueba a descomentar la sección de código comentada (líneas 19 a 22) para activar una pieza inteligente de lógica de filtrado utilizando la función `pytest.skip`, y ejecuta la prueba de nuevo...

Ahora la función `coordinate_fixture` aplica una lógica extra sobre qué combinaciones de parámetros deben usarse, sin afectar a `numbers_fixture`, o al caso de prueba.

Esto también demuestra que PyTest responde a `skip` en cualquier momento - incluso si se llama dentro de un fixture, antes de que hayamos entrado en un caso de prueba, permitiéndonos evitar cualquier combinación no deseada. Esta es otra pista de cómo funciona PyTest, internamente: Nuestros casos de prueba son simplemente especificaciones para las pruebas que PyTest ejecutará, y podemos omitir condicionalmente una prueba en cualquier punto antes de que se complete (pasando o fallando).

En este ejemplo, hemos añadido nuestra lógica de filtrado a uno de nuestros fixtures parametrizados... Pero podríamos abstraerlo aún más en un `letter_fixture` y un `number_fixture` que produzcan parámetros, y un tercer `coordinate_fixture` más específico que dependa de ellos, que añada la lógica de filtrado, y que no tenga parámetros propios, y que el caso de prueba dependa sólo de él. Si esperamos utilizar nuestros dos fixtures parametrizados por separado, esta podría ser una forma aún mejor de organizarlos.

Por último, esto también puede servir como ejemplo de cómo las dependencias de fixture no son del todo diferentes a un `import` - Si añades el `number_fixture` como argumento para (y dependencia de) `test_advanced_fixtureception`, ¿qué esperas que pueda salir mal?

Aunque esto parece que podría ser problemático - El caso de prueba ahora depende de `number_fixture` dos veces, tanto directamente con un argumento con nombre, como indirectamente a través de `coordinates_fixture` - PyTest es sorprendentemente tranquilo al respecto.

Podrías esperar que esto resultara en que `number_fixture` fuera invocado dos veces, duplicando nuestras pruebas resultantes, o incluso multiplicándolas por otra copia de nuestro parámetro extra... Pero PyTest reconoce que ambas dependencias se refieren al mismo fixture, y ese fixture (por defecto) se ejecuta una vez por caso de prueba, y así obtenemos los mismos resultados que si nuestro `number_fixture` fuera referido sólo una vez.

### A continuación:

[Revisando Fixtures](https://github.com/INGCOM-UNRN/intro-a-pytest/blob/master/tutorials/12_reviewing_fixtures.md)
