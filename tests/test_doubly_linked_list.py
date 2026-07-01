from doubly_linked_list import DoublyLinkedList
import pytest


# ---------- 기본 ----------

def test_empty_list_has_zero_length():
    """갓 생성한 리스트는 길이 0."""
    lst = DoublyLinkedList()
    assert len(lst) == 0


def test_empty_list_iterates_to_nothing():
    """빈 리스트를 순회하면 아무것도 안 나온다."""
    lst = DoublyLinkedList()
    assert list(lst) == []
    assert list(reversed(lst)) == []


# ---------- append ----------

def test_append_increases_length():
    """append할 때마다 길이가 1씩 증가."""
    lst = DoublyLinkedList()
    lst.append(10)
    lst.append(20)
    assert len(lst) == 2


def test_append_preserves_order():
    """append한 순서대로 인덱스에 들어간다."""
    lst = DoublyLinkedList()
    for x in [10, 20, 30]:
        lst.append(x)
    assert lst[0] == 10
    assert lst[1] == 20
    assert lst[2] == 30


def test_append_to_empty_sets_head_and_tail():
    """빈 리스트에 append하면 head/tail이 같은 노드를 가리킨다."""
    lst = DoublyLinkedList()
    lst.append(42)
    assert lst._head is lst._tail
    assert lst._head.data == 42


# ---------- prepend ----------

def test_prepend_to_empty_list():
    """빈 리스트에 prepend하면 head/tail이 같은 노드."""
    lst = DoublyLinkedList()
    lst.prepend(10)
    assert len(lst) == 1
    assert lst[0] == 10
    assert lst._head is lst._tail


def test_prepend_adds_to_front():
    """prepend는 맨 앞에 들어간다 (append와 반대 방향)."""
    lst = DoublyLinkedList()
    lst.append(20)
    lst.append(30)
    lst.prepend(10)
    assert lst[0] == 10
    assert lst[1] == 20
    assert lst[2] == 30
    assert len(lst) == 3


def test_prepend_reverses_insertion_order():
    """연속 prepend하면 넣은 순서의 역순이 된다."""
    lst = DoublyLinkedList()
    for x in [10, 20, 30]:
        lst.prepend(x)
    assert lst[0] == 30
    assert lst[1] == 20
    assert lst[2] == 10


# ---------- __getitem__ ----------

def test_getitem_out_of_range_raises():
    """범위 밖 인덱스는 IndexError (index == size 포함)."""
    lst = DoublyLinkedList()
    lst.append(10)
    with pytest.raises(IndexError):
        lst[1]  # size와 같은 인덱스도 거부돼야 함


def test_getitem_negative_index_raises():
    """음수 인덱스도 현재 구현에선 거부 (0 <= index 조건)."""
    lst = DoublyLinkedList()
    lst.append(10)
    with pytest.raises(IndexError):
        lst[-1]


def test_single_element_access():
    """노드 하나짜리 리스트의 경계 동작."""
    lst = DoublyLinkedList()
    lst.append(42)
    assert len(lst) == 1
    assert lst[0] == 42


# ---------- 양방향 순회 ----------

def test_iter_forward_order():
    """__iter__는 head부터 앞으로 순회."""
    lst = DoublyLinkedList()
    for x in [10, 20, 30]:
        lst.append(x)
    assert list(lst) == [10, 20, 30]


def test_reversed_backward_order():
    """__reversed__는 tail부터 뒤로 순회 (prev 필드의 보상)."""
    lst = DoublyLinkedList()
    for x in [10, 20, 30]:
        lst.append(x)
    assert list(reversed(lst)) == [30, 20, 10]


def test_iter_and_reversed_are_mirror():
    """앞 순회와 뒤 순회는 서로 뒤집힌 관계."""
    lst = DoublyLinkedList()
    for x in [1, 2, 3, 4]:
        lst.append(x)
    assert list(lst) == list(reversed(list(reversed(lst))))


# ---------- pop ----------

def test_pop_returns_last_and_shrinks():
    """pop은 꼬리 데이터를 반환하고 길이를 줄인다."""
    lst = DoublyLinkedList()
    for x in [10, 20, 30]:
        lst.append(x)
    assert lst.pop() == 30
    assert len(lst) == 2
    assert list(lst) == [10, 20]


def test_pop_keeps_links_consistent():
    """pop 후에도 양방향 순회가 둘 다 일관적이어야 한다."""
    lst = DoublyLinkedList()
    for x in [10, 20, 30]:
        lst.append(x)
    lst.pop()
    assert list(lst) == [10, 20]
    assert list(reversed(lst)) == [20, 10]  # 뒤 방향도 안 깨졌나


def test_pop_single_element_empties_list():
    """원소 하나를 pop하면 head/tail 둘 다 None이 된다."""
    lst = DoublyLinkedList()
    lst.append(42)
    assert lst.pop() == 42
    assert len(lst) == 0
    assert lst._head is None
    assert lst._tail is None


def test_pop_from_empty_raises():
    """빈 리스트에서 pop하면 IndexError."""
    lst = DoublyLinkedList()
    with pytest.raises(IndexError):
        lst.pop()


# ---------- popleft ----------

def test_popleft_returns_first_and_shrinks():
    """popleft는 머리 데이터를 반환하고 길이를 줄인다."""
    lst = DoublyLinkedList()
    for x in [10, 20, 30]:
        lst.append(x)
    assert lst.popleft() == 10
    assert len(lst) == 2
    assert list(lst) == [20, 30]


def test_popleft_keeps_links_consistent():
    """popleft 후에도 양방향 순회가 둘 다 일관적이어야 한다."""
    lst = DoublyLinkedList()
    for x in [10, 20, 30]:
        lst.append(x)
    lst.popleft()
    assert list(lst) == [20, 30]
    assert list(reversed(lst)) == [30, 20]


def test_popleft_single_element_empties_list():
    """원소 하나를 popleft하면 head/tail 둘 다 None이 된다."""
    lst = DoublyLinkedList()
    lst.append(42)
    assert lst.popleft() == 42
    assert len(lst) == 0
    assert lst._head is None
    assert lst._tail is None


def test_popleft_from_empty_raises():
    """빈 리스트에서 popleft하면 IndexError."""
    lst = DoublyLinkedList()
    with pytest.raises(IndexError):
        lst.popleft()


# ---------- 생애주기 (복합 시나리오) ----------

def test_fill_empty_refill_stays_consistent():
    """채우고 -> 다 비우고 -> 다시 채워도 상태가 일관적."""
    lst = DoublyLinkedList()
    for x in [1, 2, 3]:
        lst.append(x)
    while len(lst) > 0:
        lst.pop()
    assert lst._head is None and lst._tail is None
    # 비운 뒤 재사용
    lst.append(99)
    lst.prepend(88)
    assert list(lst) == [88, 99]
    assert list(reversed(lst)) == [99, 88]


def test_mixed_operations_keep_both_directions():
    """append/prepend/pop/popleft를 섞어도 양방향이 안 깨진다."""
    lst = DoublyLinkedList()
    lst.append(2)       # [2]
    lst.prepend(1)      # [1, 2]
    lst.append(3)       # [1, 2, 3]
    lst.popleft()       # [2, 3]
    lst.pop()           # [2]
    lst.append(4)       # [2, 4]
    assert list(lst) == [2, 4]
    assert list(reversed(lst)) == [4, 2]
    assert len(lst) == 2