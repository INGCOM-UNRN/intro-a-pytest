## 2: Afirmaciones Especiales

Sin embargo, no todo puede ser expresado como una simple aserción, pero no temas - PyTest proporciona:

[tests/02_special_assertions_test.py]((https://github.com/INGCOM-UNRN/intro-a-pytest/blob/master/tests/02_special_assertions_test.py)

```
pytest tests/02_special_assertions_test.py
```
Dos de estas pruebas lanzan excepciones a propósito - podemos usar el gestor de contexto `pytest.raises` para afirmar que suceden (y manejar esa excepción, para que no aparezca como un fallo). Por ejemplo, si cambias la línea 9 por `x = 1/1`, PyTest fallará la prueba, ya que la excepción esperada no se ha producido. (¡y lo explicará en detalle en la consola!)

En `test_keyerror_details`, también asignamos la excepción a una variable usando `as`, para que podamos referirnos a ella después del bloque `pytest.raises` - podemos inspeccionarla con más detalle, o incluso `assert` que tiene las cualidades que esperamos. Esto es muy útil cuando se quiere comprobar el comportamiento específico de las excepciones.

Por último, en `test_approximate_matches`, utilizamos `pytest.approx` para ayudar a afirmar que nuestros dos valores son "aproximadamente" iguales, aunque no sea exacto debido a la diversión con las matemáticas en coma flotante. (También podemos ajustar lo "cerca" que queremos que esté la coincidencia antes de que falle la prueba - Para más detalles, consulte la [documentación de pytest.approx](https://docs.pytest.org/en/latest/reference.html#pytest-approx).)

### A continuación:

[Repaso de lo Basico](https://github.com/INGCOM-UNRN/intro-a-pytest/blob/master/tutorials/03_reviewing_the_basics.md)
