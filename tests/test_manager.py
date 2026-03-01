import pytest
from src.id_manager.manager import IDManager

def test_id_manager_initialization():
    manager = IDManager()
    assert manager.current_id == 0
    assert manager.step == 1

    manager = IDManager(start=10, step=2)
    assert manager.current_id == 10
    assert manager.step == 2

    with pytest.raises(ValueError):
        IDManager(step=0)

def test_id_manager_get_next_id():
    manager = IDManager(start=0, step=1)
    assert manager.get_next_id() == 0
    assert manager.get_next_id() == 1
    assert manager.current_id == 2

    manager = IDManager(start=5, step=3)
    assert manager.get_next_id() == 5
    assert manager.current_id == 8
    assert manager.get_next_id() == 8
    assert manager.current_id == 11

def test_id_manager_reset():
    manager = IDManager(start=10, step=2)
    manager.get_next_id() 
    assert manager.current_id == 12
    manager.reset()
    assert manager.current_id == 0

    manager.get_next_id()
    manager.reset(start=100)
    assert manager.current_id == 100

def test_id_manager_str_repr():
    manager = IDManager(start=10, step=2)
    assert str(manager) == "IDManager(current_id=10, step=2)"
    assert repr(manager) == "IDManager(current_id=10, step=2)"
    manager.get_next_id()
    assert str(manager) == "IDManager(current_id=12, step=2)"
    assert repr(manager) == "IDManager(current_id=12, step=2)"
