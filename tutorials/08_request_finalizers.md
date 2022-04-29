
## 8: Request "finalizer" Callbacks

A veces queremos ejecutar una función de "limpieza" después de que la prueba se haya completado: Ya hemos cubierto una manera muy fácil de hacer esto usando `yield` [dentro de un fixture](), pero notamos que no es la opción más segura, si algo va mal dentro de nuestro fixture...

Afortunadamente, PyTest tiene un plugin `request` (un fixture global incorporado) que, entre otras cosas, puede usarse para añadir un "finalizador", una función que está garantizada para ser llamada después de que el fixture (y la(s) prueba(s) que dependen de él) se ejecuten... Incluso en el peor de los casos, en el que nuestro fixture en sí mismo falla, y lanza una excepción no manejada:

[tests/07_request_finalizer_test.py](https://github.com/INGCOM-UNRN/intro-a-pytest/blob/master/tests/07_request_finalizer_test.py)

```
pytest -vs tests/07_request_finalizer_test.py
```

Como siempre, podemos ver que nuestro fixture se ejecuta primero (incluyendo una llamada a una función "arriesgada"), seguido de nuestro caso de prueba, y finalmente nuestra función safe_cleanup. Una de las ventajas de este enfoque es que podemos reutilizar una función de limpieza compartida, pero el principal beneficio es que incluso si nuestro fixture falla en la inicialización, ¡nuestra función finalizadora de "limpieza" sigue ejecutándose!

Para ver realmente el finalizador en acción, descomenta la línea 11 en `07_request_finalizer_test.py` (por ejemplo, la llamada "raise Exception" comentada), y vuelve a ejecutar la prueba utilizando el comando anterior.

Esa función "arriesgada" no funcionó - ¡descarriló nuestro fixture, y nuestro caso de prueba ni siquiera se ejecutó! Pero a pesar de todo, nuestra función `safe_cleanup` fue llamada.

Y en una prueba real, con un fixture que establece algo complicado o costoso (y que podría fallar _después_ de haber hecho algún tipo de lío), ¡la limpieza garantizada podría ser una distinción realmente importante!

### A continuación:

[Intro to Parameters](https://github.com/INGCOM-UNRN/intro-a-pytest/blob/master/tutorials/09_intro_to_parameters.md)