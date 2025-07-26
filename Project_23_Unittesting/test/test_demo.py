import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app.demo import add

def test_add():
    assert add(10,20)==30