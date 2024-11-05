import pytest
from calculator import add,sub,multiply,divide

def test_add():
    assert add(1,2)==3
    assert add(-1,1)==0
    assert add(2,3)==5
    
def test_sub():
    assert sub(-1,-2)==1
    assert sub(0,0)==0
    assert sub(3,5)==-2
def test_multiply():
    assert multiply(-1,-1)==1
    assert multiply(200,0)==0
def test_divide():
    assert divide(6,3)==2
    assert divide(5,2)==2.5
    # assert divide(1,0)==0