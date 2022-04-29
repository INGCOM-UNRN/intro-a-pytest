import pytest


def test_with_local_fixture(local_fixture):
    """
    Los fixtures pueden ser invocados simplemente teniendo un 
    argumento posicional con el mismo nombre que un fixture:
    """
    print("Ejecutando test_with_local_fixture...")
    assert True


@pytest.fixture
def local_fixture():
    """
    Los accesorios son callables decorados con @fixture
    """
    print("\n(Haciendo cosas de configuración local del fixture!)")


def test_with_global_fixture(global_fixture):
    """
    Los fixtures pueden ser compartidos entre archivos de prueba (ver conftest.py)
    """
    print("Ejecutando test_with_global_fixture...")
