from doubly_linked_list import DoublyLinkedList

class Stack:
    """LIFO 스택. DoublyLinkedList를 내부에 들고 head 쪽을 top으로 사용한다 (컴포지션)."""
    
    def __init__(self):
        self._list = DoublyLinkedList()
        
    def __len__(self):
        return len(self._list)
    
    def is_empty(self):
        return len(self._list) == 0
    
    def push(self, value):
        """top(head)에 삽입. O(1)."""
        self._list.prepend(value)
        
    def pop(self):
        """top(head) 제거 후 반환. O(1). 빈 스택이면 popleft가 IndexError를 전파한다."""
        return self._list.popleft()
    
    def peek(self):
        """top 값을 제거 없이 반환. O(1). 빈 스택이면 IndexError."""
        if self.is_empty():
            raise IndexError("peek from an empty stack")
        return self._list[0]
    
    def __iter__(self):
        """top -> bottom 순서로 순회."""
        # yield from <어떤 객체>는 그 객체가 반복 가능(iterable)일 때만 동작한다.
        # Double Linked List에 __iter__을 만들어놨기 때문에 이게 가능
        # 없었으면 'DoublyLinkedList' object is not iterable로 터졌을 것임
        yield from self._list
    
    def __repr__(self):
        return f"Stack([{', '.join(repr(v) for v in self)}])"