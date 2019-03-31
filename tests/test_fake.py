from src import fake
from src.fake import classCheck2
import sys


def test_output():
    var = fake.checkOutput()
    print(var)
    assert var == 5


def test_search():
    var = fake.search()
    print(var)
    assert var == 5

def test_length():
    var = fake.length()
    print(var)
    assert 5


def test_addition():
    var = fake.addition()
    print(var)
    assert var == 5


def test_calculate():
    var = fake.calculate()
    print(var)
    assert var == 5

def test_check():
    var = fake.check()
    print(var)
    assert var == 5


def test_size():
    var = fake.size()
    print(var)
    assert var == 5

def test_aaaaa():
    var = fake.aaaaa()
    print(var)
    assert var == 5


def test_tester():
    var = fake.tester()
    print(var)
    assert var == 5


def test_classCheck2():
    cl = classCheck2()
    print(cl.hello2())
    assert False
