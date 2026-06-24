import ctypes

class DynamicArray:
    def __init__(self):
        self._n = 0 # 현재 저장된 원소 개수
        self._capacity = 1 # 현재 배열의 칸 수
        self._A = self._make_array(self._capacity)
        
    def __len__(self):
        """저장된 원소 개수. len(arr)로 호출됨. O(1)"""
        return self._n
    
    def __getitem__(self, index):
        """arr[index]로 호출됨. O(1)"""
        # TODO : 범위 체크 후 self._A[index] 반환
        if not 0 <= index < self._n:
            raise IndexError("index out of range")
        return self._A[index]
    
    def append(self, value):
        """맨 뒤에 추가. """
        # 맨 뒤에 추가. 꽉 차면 resize. 평균 O(1)
        # 왜 이게 O(1)인가? resize라는 O(n)을 가지고 있는데?
        # 정답은 분할상환(amortized) O(1)
        # 자료구조를 다룰 때 가끔 발생하는 매우 비싼 연산 비용을, 일련의 여러 연산들 전체에 평균화하여 계산하는 방식
        if self._n == self._capacity:
            self.resize(2 * self._capacity)
        self._A[self._n] = value
        self._n += 1
    
    def resize(self, new_capacity):
        # 더 큰 배열로 갈아탄다. O(n)
        B = self._make_array(new_capacity) # 새 배열(더 큼)
        for i in range(self._n): # 기존 값들을
            B[i] = self._A[i] # 하나씩 복사
        self._A = B # 새 배열로 교체
        self._capacity = new_capacity # 용량 갱신
    
    def _make_array(self, capacity):
        return (capacity * ctypes.py_object)()
    
if __name__ == "__main__":
    arr = DynamicArray()
    for i in range(10):
        arr.append(i)
        print(f"len={len(arr)}, capacity={arr._capacity}")
    print(arr[3], arr[9])