## 7: La fixture "petición" 

Los Fixtures son muy potentes, no sólo porque PyTest puede ejecutarlos automáticamente, sino porque pueden ser "conscientes" del contexto en el que se están utilizando.

(Y también, como vamos a ver, los Fixtures pueden depender de otros Fixtures, lo que permite un comportamiento realmente interesante...)

En este ejemplo, escribiremos un fixture que aprovecha el fixture `request` incorporado (también conocido como "Plugin", un fixture estándar que está disponible globalmente para todos los tests de PyTest) para aprender más sobre cómo está siendo llamado:

[tests/06_request_test.py](Como siempre, podemos ver que nuestro fixture se ejecuta primero (incluyendo una llamada a una función "arriesgada"), seguido de nuestro caso de prueba, y finalmente nuestra función safe_cleanup. Una de las ventajas de este enfoque es que podemos reutilizar una función de limpieza compartida, pero el principal beneficio es que incluso si nuestro fixture falla en la inicialización, ¡nuestra función finalizadora de "limpieza" sigue ejecutándose!

Para ver realmente el finalizador en acción, descomenta la línea 11 en `07_request_finalizer_test.py` (por ejemplo, la llamada "raise Exception" comentada), y vuelve a ejecutar la prueba utilizando el comando anterior.

Esa función "arriesgada" no funcionó - ¡descarriló nuestro fixture, y nuestro caso de prueba ni siquiera se ejecutó! Pero a pesar de todo, nuestra función `safe_cleanup` fue llamada.

Y en una prueba real, con un fixture que establece algo complicado o costoso (y que podría fallar _después_ de haber hecho algún tipo de lío), ¡la limpieza garantizada podría ser una distinción realmente importante!
/blob/master/tests/06_request_test.py)

```
pytest -vs tests/06_request_test.py
```

Entre otras cosas, nuestro fixture puede decir que está siendo invocado a nivel de función (por ejemplo, está siendo referenciado directamente por una función del caso de prueba), sabe en qué "nodo" se está ejecutando actualmente (en un sentido de árbol de dependencia: sabe qué caso de prueba lo está llamando), y sabe en qué Módulo se está ejecutando, que en este caso es el archivo `06_request_test.py`.

Además de proporcionar el contexto, el fixture `request` también se puede utilizar para influir en el comportamiento de PyTest mientras ejecuta nuestras pruebas...

### A continuación:

[Request "finalizer" Callbacks](https://github.com/INGCOM-UNRN/intro-a-pytest/blob/master/tutorials/08_request_finalizers.md)