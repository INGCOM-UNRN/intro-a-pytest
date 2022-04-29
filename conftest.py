from __future__ import print_function
from pytest import fixture


@fixture
def global_fixture():
    print("\n(Haciendo preparativos globales de fixtures!)")


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "db: Marca de ejemplo para etiquetar tests relacionados con Bases de Datos"
    )
    config.addinivalue_line(
        "markers", "slow: Marca de ejemplo para etiquetar los tests mas lentos"
    )
