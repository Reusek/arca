import arca

def test_typeguard():
    a = arca.serialize("csv")
    assert a == "csv"

