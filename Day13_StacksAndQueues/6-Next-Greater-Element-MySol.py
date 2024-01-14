class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans  = []
        stk = []
        h = {}
        top = -1
        n2 = len(nums2)
        # Start from the end and push element in the stack
        for i in range(n2-1,-1,-1):
            # If the stack is empty then assign -1 to the elment as no element is greater than the present element.
            if top == -1:
                h[nums2[i]] = -1
            elif stk[top] > nums2[i]:
                h[nums2[i]] = stk[top]
            else:
                stk.pop()
                top-=1
                while(top>-1):
                    if stk[top] > nums2[i]:
                        h[nums2[i]] = stk[top]
                        break
                    stk.pop()
                    top-=1
                if top == -1:
                    h[nums2[i]] = -1
            stk.append(nums2[i])
            top+=1

        for i in nums1:
            ans.append(h[i])
        return ans