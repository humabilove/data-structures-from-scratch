from dynamic_array import DynamicArray
import pytest

def test_empty_array():
    arr = DynamicArray()
    assert len(arr) == 0
    
def test_append_increases_length():
    arr = DynamicArray()
    arr.append(10)
    arr.append(20)
    assert len(arr) == 2
    
def test_getitem_returns_value():
    arr = DynamicArray()
    arr.append(10)
    arr.append(20)
    assert arr[0] == 10
    assert arr[1] == 20
    
def test_capacity_doubles():
    arr = DynamicArray()
    arr.append(1) # capacity 1
    arr.append(2) # 1 -> 2
    arr.append(3) # 2 -> 4
    assert arr._capacity == 4
    
def test_getitem_out_of_range_raises():
    arr = DynamicArray()
    arr.append(10)
    with pytest.raises(IndexError):
        arr[5]
