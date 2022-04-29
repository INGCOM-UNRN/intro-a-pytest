### 3: Reviewing the Basics

* Los casos de PyTest pueden ser tan simples como una función cuyo nombre comienza con "test", en un archivo cuyo nombre comienza con "test".

    * (PyTest también encontrará y ejecutará pruebas de estilo xUnit creadas con el módulo estándar `unittest`, permitiéndote empezar a usar PyTest junto con las pruebas existentes.
    
    * El comportamiento de búsqueda de pruebas tiene valores predeterminados razonables, pero es [¡extremadamente configurable!](https://docs.pytest.org/en/latest/goodpractices.html#conventions-for-python-test-discovery).

* Un caso de PyTest pasará si:
    * Sus aserciones son True
    * (O no tiene ninguna aserción)
    * Y si no genera ninguna Excepción no manejada.

* (PyTest se puede utilizar para "ejercitar" el código, e informará de los errores, incluso sin ninguna aserción real)

* PyTest utiliza la palabra clave básica de Python `assert`, pero hará una introspección en su código y "desempaquetará" información útil sobre por qué falló la aserción.

    * (Si su caso de PyTest llama a otro código que hace aserciones, éstas serán honradas también (en el sentido de que cualquier aserción fallida resultante de su prueba causará que la prueba sea reportada como "fallida").
    
    * Sin embargo, las aserciones que no son locales (por ejemplo, que no se encuentran dentro de su función de prueba) no serán "desempaquetadas" y explicadas en detalle. Si tus pruebas llaman a otro código que realiza aserciones, debes hacer que esas aserciones "externas" sean lo más claras posible: Intenta limitar cada aserción a una comprobación específica, y proporciona un mensaje de error como segundo argumento, para que el fallo sea más fácil de entender.

        * Por ejemplo, si quiere afirmar que x es mayor que cero, y divisible por 2, en una función que es llamada por uno de sus casos de prueba (¡pero que no está dentro de una función de caso de prueba de python!) considere algo como

        ```
        assert (x > 0), "X debe ser > 0, pero es {}".format(x)
        assert not (x % 2), "X debe ser divisible por 2, pero es {}".format(x)
        ```

        (Pero si es posible, haz todas tus aserciones dentro de los casos de prueba, para que PyTest pueda documentar sus razones de fallo y su contexto por ti).

* PyTest proporciona características para "esperar" Excepciones, y coincidir con valores aproximadamente similares, similar a [unittest.TestCase](https://docs.python.org/2/library/unittest.html#basic-example):

    * [pytest.raises](https://docs.pytest.org/en/latest/reference.html#pytest-raises)

    * [pytest.approx](https://docs.pytest.org/en/latest/reference.html#pytest-approx)

### A continuación:

[Introducción a Fixtures](https://github.com/INGCOM-UNRN/intro-a-pytest/blob/master/tutorials/04_intro_to_fixtures.md)
