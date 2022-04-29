import pytest


def test_div_zero_exception():
    """
    pytest.raises puede afirmar que se produce una excepción (atajandola)
    """
    with pytest.raises(ZeroDivisionError):
        x = 1 / 0


def test_keyerror_details():
    """
    La excepción generada puede ser referenciada, y posteriormente inspeccionada (o afirmada)
    """
    my_map = {"foo": "bar"}

    with pytest.raises(KeyError) as ke:
        baz = my_map["baz"]

    # Nuestro KeyError debería hacer referencia a la clave que falta, "baz"
    assert "baz" in str(ke)


def test_approximate_matches():
    """
    pytest.approx puede utilizarse para afirmar una igualdad numérica "aproximada"
    (compará con "assertAlmostEqual" en unittest.TestCase)
    """
    assert 0.1 + 0.2 == pytest.approx(0.3)
