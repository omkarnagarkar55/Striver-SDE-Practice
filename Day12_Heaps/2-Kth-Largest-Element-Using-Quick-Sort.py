class Solution:
    def findKthLargest(self, arr: List[int], k: int) -> int:
        left = 0
        right = len(arr) - 1
        kth = 0
        while 1:
            idx = self.partition(arr, left, right)
            if idx == k - 1:
                kth = arr[idx]
                break
            if idx < k - 1:
                left = idx + 1
            else:
                right = idx - 1
        return kth

    def partition(self,arr: List[int], left: int, right: int) -> int:
        pivot = arr[left]
        l = left + 1
        r = right
        while l <= r:
            if arr[l] < pivot and arr[r] > pivot:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1
            if arr[l] >= pivot:
                l += 1
            if arr[r] <= pivot:
                r -= 1

        arr[left], arr[r] = arr[r], arr[left]
        return r
    