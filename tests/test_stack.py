import pytest

from stack import Stack


# ── 생성 / 빈 상태 ──────────────────────────────
def test_new_stack_is_empty():
    s = Stack()
    assert len(s) == 0
    assert s.is_empty() is True


def test_pop_empty_raises():
    s = Stack()
    with pytest.raises(IndexError):
        s.pop()


def test_peek_empty_raises():
    s = Stack()
    with pytest.raises(IndexError):
        s.peek()


# ── push ────────────────────────────────────────
def test_push_increases_len():
    s = Stack()
    s.push(1)
    assert len(s) == 1
    assert s.is_empty() is False
    s.push(2)
    assert len(s) == 2


def test_push_does_not_remove():
    """push는 top만 바꾸고 아무것도 안 지운다."""
    s = Stack()
    s.push(10)
    s.push(20)
    assert len(s) == 2  # 둘 다 살아있음


# ── peek ────────────────────────────────────────
def test_peek_returns_top_without_removing():
    s = Stack()
    s.push(1)
    s.push(2)
    assert s.peek() == 2       # 마지막에 넣은 게 top
    assert len(s) == 2         # peek은 안 지움 — 길이 그대로
    assert s.peek() == 2       # 다시 봐도 같음 (부작용 없음)


def test_peek_follows_top_after_push():
    s = Stack()
    s.push(1)
    assert s.peek() == 1
    s.push(2)
    assert s.peek() == 2       # top이 새로 넣은 값으로 이동


# ── pop (LIFO 핵심 + 파괴적 연산 교차 검증) ──────
def test_pop_returns_last_pushed():
    """LIFO: 마지막에 넣은 게 처음 나온다."""
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    assert s.pop() == 3
    assert s.pop() == 2
    assert s.pop() == 1
    assert s.is_empty() is True


def test_pop_updates_len_and_peek_each_step():
    """pop 한 번마다 len·peek·is_empty가 모두 일관되게 변하는지 교차 검증."""
    s = Stack()
    for v in (1, 2, 3):
        s.push(v)
    # 현재: top=3, len=3
    assert s.pop() == 3
    assert len(s) == 2
    assert s.peek() == 2       # 새 top

    assert s.pop() == 2
    assert len(s) == 1
    assert s.peek() == 1

    assert s.pop() == 1
    assert len(s) == 0
    assert s.is_empty() is True


def test_pop_then_push_again():
    """비웠다가 다시 채워도 정상 동작 (참조 꼬임 없음)."""
    s = Stack()
    s.push(1)
    s.pop()
    assert s.is_empty() is True
    s.push(99)                 # 빈 스택에 재삽입
    assert s.peek() == 99
    assert len(s) == 1


def test_pop_all_then_pop_raises():
    """다 빼낸 뒤 한 번 더 pop하면 IndexError (경계)."""
    s = Stack()
    s.push(1)
    s.pop()
    with pytest.raises(IndexError):
        s.pop()


# ── __iter__ (순회 순서 = top → bottom) ──────────
def test_iter_order_top_to_bottom():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    assert list(s) == [3, 2, 1]     # top부터


def test_iter_does_not_consume():
    """순회는 스택을 비우지 않는다 (읽기 전용)."""
    s = Stack()
    s.push(1)
    s.push(2)
    list(s)                          # 한 번 순회
    assert len(s) == 2               # 그대로
    assert list(s) == [2, 1]         # 다시 순회해도 같음


# ── __repr__ ────────────────────────────────────
def test_repr_empty():
    s = Stack()
    assert repr(s) == "Stack([])"


def test_repr_shows_top_first():
    s = Stack()
    s.push(1)
    s.push(2)
    assert repr(s) == "Stack([2, 1])"


def test_repr_uses_repr_of_elements():
    """문자열 원소는 따옴표까지 나온다 (repr of elements)."""
    s = Stack()
    s.push("a")
    assert repr(s) == "Stack(['a'])"