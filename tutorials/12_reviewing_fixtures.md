## 12: Revisando Fixtures

* Los Fixtures son el mecanismo de PyTest para controlar el "contexto" alrededor de tus casos de prueba

* PyTest viene con un número de [fixtures incorporados](https://docs.pytest.org/en/latest/reference.html#fixtures), aunque probablemente querrás crear los tuyos propios.

* Los Fixtures son típicamente funciones con el decorador @pytest.fixture:

    * Los Fixtures pueden `devolver` un valor, como una función normal, o `devolver` un valor como un generador (¡aunque sólo se permite un rendimiento!), y cualquier código posterior al rendimiento se ejecutará después de que el caso de prueba haya pasado o fallado.

    * Por defecto, un Fixture será llamado (y potencialmente devolverá o producirá un valor) una vez por cada Caso de Prueba al que esté asociado, aunque esto puede ser reconfigurado de diferentes maneras (cubierto más adelante, aunque vea la parametrización más abajo...)

    * (Si un fixture lanza una excepción no manejada, o falla de alguna manera, el caso de prueba no se ejecutará. En el caso de un fixture `yield`, esto también significa que el código post-yield tampoco se ejecutará).

    * Las fijaciones pueden definirse "localmente", en el mismo módulo que los casos de prueba que las utilizan, o "globalmente" en un archivo `conftest.py`. (En el caso de que haya múltiples implementaciones de un nombre de fixture dado, PyTest preferirá la "más local", por ejemplo, el fixture situado más cerca del caso de prueba en su estructura de archivos).

* Los casos de prueba pueden tener una "dependencia" de un fixture:

    * Teniendo un argumento de palabra clave cuyo nombre coincida con el fixture

    * (Los casos de prueba fallarán si sus argumentos con nombre no se corresponden con un fixture válido)

    * Los fixture con parámetros (`params`) pueden hacer que se creen múltiples pruebas a partir de un caso de prueba dado - Estas pruebas "parametrizadas" pueden pasar o fallar independientemente, y se denominan como los parámetros.

    * (Vale la pena señalar que las instancias de prueba en sí son los "nodos" en el gráfico de pruebas de PyTest, no las funciones de casos de prueba que has estado escribiendo - ¡Esta distinción comienza a ser más evidente con los parámetros!)

* Los Fixtures pueden ser "muy meta":

    * Las instalaciones pueden depender unas de otras...

    * Las dependencias de los fixture son similares a la "importación", en el sentido de que incluso si A depende de B y C, y B depende de C, entonces C sólo se importará (o en este caso, se instanciará) una vez para A.

    * Si un caso de prueba depende de múltiples dispositivos que tienen parámetros, el caso de prueba será llamado con el producto cartesiano completo de todos los parámetros (por ejemplo, cada combinación de todos los parámetros de los dispositivos combinados).

Los fixtures son muy complicadas, pero en última instancia son muy potentes - realmente sólo hemos rascado la superficie aquí, pero esperamos que esto le dé una visión general de lo que pueden hacer por sus pruebas.

Por ahora, pasemos a otro poderoso concepto...

### A continuación:

[Introducción al Marcado de Tests](https://github.com/pluralsight/intro-to-pytest/blob/master/tutorials/13_intro_to_test_marking.md)