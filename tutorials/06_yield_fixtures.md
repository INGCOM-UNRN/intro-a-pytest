## 6: Yield Fixtures

Aquí hay un accesorio más complicado que utiliza la palabra clave `yield` - Puede que estés más acostumbrado a ver su uso en funciones generadoras, que normalmente son llamadas repetidamente (por ejemplo, iteradas) para entregar sus valores.

Si esto parece confuso (o si no estás familiarizado con `yield`), no te preocupes: Esto es un poco diferente, pero lo importante es entender que `yield` es muy parecido a `return`, excepto por una interesante diferencia...

[tests/05_yield_fixture_test.py](https://github.com/INGCOM-UNRN/intro-a-pytest/blob/master/tests/05_yield_fixture_test.py)

```
pytest -vs tests/05_yield_fixture_test.py
```

Como la última vez, nuestro fixture se ejecutó antes que el caso de prueba que dependía de él... Hasta el momento en que llamamos a `yield`. Entonces nuestra prueba se ejecutó, recibiendo el valor "cedido" como argumento... Y entonces, _después_ de que la prueba terminara, nuestro fixture continuaba donde lo había dejado, y ejecutaba el resto del código (después de la llamada a `yield`).

Esto nos permite realizar acciones tanto antes como después de la prueba, ¡con un mínimo de código! Pero hay que tener en cuenta algunas cosas:

 * A diferencia de los generadores típicos, nuestros accesorios de rendimiento nunca deben ceder más de una vez. (Y PyTest lo impone - intente añadir un segundo yield y vea lo que sucede: ¡Alerta de Spoiler! Como con muchas de nuestras preguntas hipotéticas, el resultado es una prueba inutilizable).

    * (Si esto te hace confundirte con tus conceptos personales de generadores, trata de no leer demasiado en ello - Los Fixtures _pueden_ ser generadores, y PyTest los usará en consecuencia, pero espera que rindan exactamente una vez, y que realice la primera generación antes del caso de prueba, y la segunda generación (el código de "limpieza" después del `yield`) después de que el caso de prueba se complete.

 * Hay un caso de esquina que hay que tener en cuenta aquí: Si algo va mal _dentro_ de nuestro fixture, de forma que se lanza una excepción no controlada antes de llamar a `yield`, nunca llegaremos al código post-yield... Algo comprensible, si lo piensas.
 
    * Esto puede no ser el fin del mundo - también significa que no ejecutaremos los casos de prueba que dependen de nuestro fixture roto, así que quizás la limpieza posterior a la prueba no será tan vital.
    
    * (Esto no mata totalmente nuestra ejecución de pruebas, tampoco - Las pruebas que dependen del fixture roto fallarán durante la "configuración", pero PyTest considerará otras cosas).
    
    * (Si esto parece que puede ser problemático, dependiendo de lo que el fixture estaba tratando de hacer antes de fallar, no te preocupes: Hay algunas opciones de limpieza más completas, que discutiremos más adelante).

### A continuación:

[Request Fixtures](https://github.com/INGCOM-UNRN/intro-a-pytest/blob/master/tutorials/07_request_fixtures.md)