


from typing import List
from collections import deque

def fourSum(nums: List[int], target: int) -> List[List[int]]:
    n = len(nums) # size of the array
    st = set()

    # checking all possible quadruplets:
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for l in range(k + 1, n):
                    # taking bigger data type
                    # to avoid integer overflow:
                    sum = nums[i] + nums[j]
                    sum += nums[k]
                    sum += nums[l]

                    if sum == target:
                        temp = [nums[i], nums[j], nums[k], nums[l]]
                        temp.sort()
                        st.add(tuple(temp))

    ans = [list(x) for x in st]
    return ans

if __name__ == '__main__':
    nums = [4, 3, 3, 4, 4, 2, 1, 2, 1, 1]
    target = 9
    ans = fourSum(nums, target)
    print("The quadruplets are:")
    for it in ans:
        print("[", end="")
        for ele in it:
            print(ele, end=" ")
        print("]", end=" ")
    print() 
