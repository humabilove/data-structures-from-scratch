class _Node:
    """단일 연결 리스트의 노드. 데이터 + 다음 노드 참조."""
    # slots라고 저장하는 이유는 무엇인가? 이것도 파이썬의 약속 중 하나인가?
    __slots__ = ("data", "next") # 메모리 절약 + 오타 방지
    
    def __init__(self, data):
        self.data = data
        self.next = None
        
class SinglyLinkedList:
    def __init__(self):
        self._head = None # 첫 노드로 들어가는 유일한 입구
        self._size = 0 # __len__을 O(1)로 만들기 위해 따로 관리
        
    def __len__(self):
        """O(1). _size를 직접 반환."""
        return self._size
    
    def append(self, data):
        """꼬리에 추가. head부터 끝까지 순회 -> O(n)."""
        new_node = _Node(data)
        if self._head is None: # 빈 리스트면 새 노드가 head
            self._head = new_node
        else:
            current = self._head
            while current.next is not None: # 마지막 노드까지 전진. None이면 루프 끝내고 나감
                current = current.next
            current.next = new_node # 마지막 노트 뒤에 연결
        self._size += 1
        
    def prepend(self, data):
        """맨 앞에 추가. 포인터만 갈면 돼서 O(1)"""
        new_node = _Node(data)
        new_node.next = self._head
        self._head = new_node
        self._size += 1
        
    def __getitem__(self, index):
        """index번째 노드의 데이터. head부터 index칸 전진 -> O(n)"""
        if not 0 <= index <= self._size:
            raise IndexError("list index out of range")
        current = self._head
        for _ in range(index):
            current = current.next
        return current.data