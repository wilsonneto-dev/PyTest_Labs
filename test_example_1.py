import pytest
from examples_1 import add

def test_add():
    result = add(1, 2)
    assert result == 3
    
def test_add2():
    result = add(3,3)
    assert result == 6
    
def test_error():
    with pytest.raises(ValueError):
        add(-1, 2) 

