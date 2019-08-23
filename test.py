from balance import *

def test_arquivo():
    lista = open_arquivo()

    if lista:
        assert True
    else:
        assert False

def test_umax_ttask():
    lista = open_arquivo()
    ttask = int(lista[0])
    umax = int(lista[1])
    if umax >= 1 and umax <= 10 :
        if ttask >= 1 and ttask <= 10 :
            assert True
        else:
            assert False
    else:
        assert False


test_arquivo()
test_umax_ttask()
