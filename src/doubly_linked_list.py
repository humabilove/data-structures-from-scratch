class _Node:
    """이중 연결 리스트의 노드. 데이터 + 양쪽 이웃 참조."""
    __slots__ = ("data", "prev", "next") # 메모리 절약 + 오타 방지
    
    def __init__(self, data):
        self.data = data
        self.prev = None # 단일 리스트엔 없던 뒤 방향 화살표
        self.next = None
        
class DoublyLinkedList:
    def __init__(self):
        self._head = None # 첫 노드를 가리키는 참조 (노드를 담는 게 아님)
        self._tail = None # 마지막 노드를 가리키는 참조 -> append O(1)의 핵심
        self._size = 0
        
    def __len__(self):
        """O(1). _size를 직접 반환."""
        return self._size
    
    def __getitem__(self, index):
        """index번째 노드의 데이터. head부터 index칸 전진 -> O(n)."""
        if not 0 <= index < self._size:
            raise IndexError("List index out of range")
        else:
            current = self._head
            for _ in range(index):
                current = current.next
            return current.data
        
    def append(self, data):
        """꼬리에 추가. _tail을 직접 들고 있으니 O(1)"""
        new_node = _Node(data)
        if self._tail is None:
            # 빈 리스트면 head/tail이 같은 노드를 가리킴
            self._head = new_node
            self._tail = new_node
        else:
            # 양방향은 항상 쌍으로 갱신해주기
            new_node.prev = self._tail # 새 노드가 뒤(기존 꼬리)를 가리킴
            self._tail.next = new_node # 기존 꼬리가 앞(새 노드)을 가리킴
            self._tail = new_node # 꼬리 참조를 새 노드로 이동
        self._size += 1
        
    def prepend(self, data):
        """맨 앞에 추가. append의 대칭. O(1)."""
        new_node = _Node(data)
        if self._head is None: # 빈 리스트면 head/tail이 같은 노드를 가리킴
            self._head = new_node
            self._tail = new_node
        else:
            new_node.next = self._head # 새 노드가 앞(기존 머리)을 가리킴
            self._head.prev = new_node # 기존 머리가 뒤(새 노드)를 가리킴
            self._head = new_node # 머리 참조를 새 노드로 이동
        self._size += 1
    
    # for, list(dll), 'A' in dll, max(dll), sum(dll) 등을 사용하기 위해 정의해놓는
    # 표준 콘센트 규격. 이 규격만 맞추면 파이썬 생태계의 온갖 도구(for, list, in, max...)에 그냥 꽂힌다.
    def __iter__(self):
        """head부터 next를 따라 앞으로 순회. 제너레이터라 메모리 O(1)."""
        current = self._head
        while current is not None:
            # yield는?
            # 함수를 "값을 하나씩 흘려보내는 함수"로 바꾼다. 이런 함수를 "제너레이터"라고 부른다.
            yield current.data
            current = current.next
            
    def __reversed__(self):
        """tail부터 prev를 따라 뒤로 순회. prev 필드의 직접적 보상."""
        current = self._tail
        while current is not None:
            yield current.data
            current = current.prev
            
    def pop(self):
        """꼬리 제거 후 그 데이터 반환. tail.prev로 즉시 접근 -> O(1)."""
        if self._tail is None: # 빈 리스트면 뺄 게 없음
            raise IndexError("pop from empty list")
        data = self._tail.data
        if self._head is self._tail: # 원소가 하나뿐이면 리스트가 빔
            self._head = None
            self._tail = None
        else:
            new_tail = self._tail.prev # 끝에서 두 번째 노드 (O(1))
            new_tail.next = None # 새 꼬리의 앞 화살표를 끊음
            self._tail.prev = None # 떨어져나간 노드의 참조도 정리
            self._tail = new_tail # 꼬리 참조 이동
        self._size -= 1
        return data
    
    def popleft(self):
        """머리 제거 후 그 데이터 반환. pop의 대칭. O(1)."""
        if self._head is None: # 빈 리스트면 뺼 게 없음
            raise IndexError("pop from empty list")
        data = self._head.data
        if self._head is self._tail: # 원소가 하나뿐이면 리스트가 빔
            self._head = None
            self._tail = None
        else:
            new_head = self._head.next # 두 번째 노드 (O(1))
            new_head.prev = None # 새 머리의 뒤 화살표를 끊음
            self._head.next = None # 떨어져나간 노드의 참조도 정리
            self._head = new_head # 머리 참조 이동
        self._size -= 1
        return data