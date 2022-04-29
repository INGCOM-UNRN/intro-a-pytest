from other_code.services import DATA_SET_A, DATA_SET_B, DATA_SET_C


def test_example():
    """
    Pero en realidad, los casos de prueba deben ser callables que contengan aserciones:
    """
    print("\nEjecución de test_example...")
    assert DATA_SET_A == DATA_SET_B
