from singly_linked_list import SinglyLinkedList
import pytest

def test_empty_list_has_zero_length():
    """갓 생성한 리스트는 길이 0."""
    lst = SinglyLinkedList()
    assert len(lst) == 0
    
def test_append_increases_length():
    """append할 때마다 길이가 1씩 증가"""
    lst = SinglyLinkedList()
    lst.append(10)
    lst.append(20)
    assert len(lst) == 2
    
def test_append_preserves_order():
    """append한 순서대로 인덱스에 들어간다 (FIFO 순서 유지)"""
    lst = SinglyLinkedList()
    for x in [10, 20, 30]:
        lst.append(x)
    assert lst[0] == 10
    assert lst[1] == 20
    assert lst[2] == 30
    
def test_getitem_out_of_range_raises():
    """범위 밖 인덱스는 IndexError."""
    lst = SinglyLinkedList()
    lst.append(10)
    with pytest.raises(IndexError):
        lst[5]

def test_getitem_negative_index_raises():
    """음수 인덱스도 현재 구현에선 거부 (0 <= index 조건)."""
    lst = SinglyLinkedList()
    lst.append(10)
    with pytest.raises(IndexError):
        lst[-1]
        
def test_single_element_access():
    """노드 하나짜리 리스트의 경계 동작."""
    lst = SinglyLinkedList()
    lst.append(42)
    assert len(lst) == 1
    assert lst[0] == 42
    
def test_prepend_to_empty_list():
    """빈 리스트에 prepend하면 그게 head이자 유일한 노드."""
    lst = SinglyLinkedList()
    lst.prepend(10)
    assert len(lst) == 1
    assert lst[0] == 10
    
def test_prepend_adds_to_front():
    """prepend는 맨 앞에 들어간다 (append와 반대 방향)."""
    lst = SinglyLinkedList()
    lst.append(20)
    lst.append(30)
    lst.prepend(10)
    assert lst[0] == 10
    assert lst[1] == 20
    assert lst[2] == 30
    assert len(lst) == 3
    
def test_prepend_reverses_insertion_order():
    """연속 prepend하면 넣은 순서의 역순이 된다."""
    lst = SinglyLinkedList()
    for x in [10, 20, 30]:
        lst.prepend(x)
    assert lst[0] == 30
    assert lst[1] == 20
    assert lst[2] == 10