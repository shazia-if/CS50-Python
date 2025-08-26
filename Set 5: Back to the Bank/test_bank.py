import pytest
from bank import value

def test_hello():
    assert value("hello")==0
    assert value("HELLO")==0

def test_Hwords():
    assert value("Hey")==20
    assert value("high")==20
    assert value("HOPE")==20

def test_otherwords():
    assert value("Good")== 100
    assert value("AMAZING")==100
    assert value("irony")==100
