import cli


def test_obtener_clima():
    assert cli.obtener_clima("Asuncion", "json") is not None
