## 10: Parametro-ception!

Python incluye un increíble conjunto de herramientas de iteración, incluyendo funciones que hacen que sea sencillo generar todas las combinaciones y permutaciones posibles de un conjunto de datos - Estamos a punto de ver un ejemplo interesante de este tipo de comportamiento, utilizando múltiples accesorios parametrizados.

Es mucho más fácil de demostrar que de explicar, así que empecemos por eso: Aquí hay otro caso de prueba simple, que depende de dos fixtures - Y vale la pena notar que cada uno de esos fixtures tiene su propio conjunto de parámetros:

[tests/09_params-ception_test.py](https://github.com/pluralsight/intro-to-pytest/blob/master/tests/09_params-ception_test.py)

```
pytest -vs tests/09_params-ception_test.py
```

¿Cómo es que dos conjuntos de 4 parámetros se han convertido en 16 pruebas? La respuesta corta es que estamos experimentando el [Producto Cartesiano](https://en.wikipedia.org/wiki/Cartesian_product) de nuestros parámetros de fixture.

Pero la respuesta menos intensiva en teoría de conjuntos es que nuestro caso de prueba depende de "letters_fixture", que hace que PyTest produzca una prueba para cada parámetro de letras... Y también depende de `numbers_fixture`, que a su vez quiere repetir cada prueba con cada uno de sus propios parámetros numéricos.

Esto es evidente por el orden en que se ejecutan las pruebas, y (¡gracias a PyTest!) por las etiquetas de esas pruebas: Podemos ver que nuestra prueba se ejecuta primero con nuestra `fijación_de_letras`, y cada uno de sus parámetros (empezando por "a"), y esas ejecuciones se "multiplican" por la `fijación_de_letras`, que se asegura de que sus propias pruebas se repitan para cada uno de sus propios parámetros (empezando por "1").

Como resultado, nuestra función de caso de prueba único se ejecuta como un total de dieciséis pruebas, una para cada combinación de los cuatro números y cuatro letras (4 x 4 = 16).

Aunque _podríamos_ hacer un único fixture que diera cada combinación como parámetro ('a1', 'a2', 'a3', etc.), mantenerlos como fixtures separados reduce la huella de esos parámetros en nuestro código, dejándolo algo más fácil de leer (en el sentido de que dos listas de cuatro ocupan la mitad de espacio que una lista completa de dieciséis).

Pero estos parámetros individuales también podrían reutilizarse y componerse en diferentes pruebas, lo que permitiría una mayor flexibilidad, especialmente si las letras o los números tuvieran que referenciarse por sí solos. Imagínese que necesita un dispositivo que pruebe 234 combinaciones únicas de letras y dígitos, y que más tarde decide eliminar todos los conjuntos con vocales, o todos los conjuntos que contienen el número 3. ¿No sería más limpio y fácil operar con dos subconjuntos más pequeños (la lista de las 26 letras y la lista de los 9 dígitos) que se combinan para producir esos datos?

Pero hay una forma aún más elegante de resolver ese problema en particular, continuando con la ventaja de que los conjuntos pueden, a su vez, depender de otros conjuntos...

### A continuación:

[Parametro-ception avanzada!](https://github.com/pluralsight/intro-to-pytest/blob/master/tutorials/11_advanced_parameter-ception.md)
