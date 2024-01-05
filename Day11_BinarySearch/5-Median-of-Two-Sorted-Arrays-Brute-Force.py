class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combi = []
        n = len(nums1)
        m = len(nums2)

        a = 0
        b = 0
        while(a<n and b<m):
            if nums1[a] <= nums2[b]:
                combi.append(nums1[a])
                a+=1
            else:
                combi.append(nums2[b])
                b+=1

        while(a<n):
            combi.append(nums1[a])
            a+=1

        while(b<m):
            combi.append(nums2[b])
            b+=1
        print(combi)
        if (n + m) % 2 == 1:
            return combi[int((n+m)//2)]
        else:
            return (combi[int((n+m - 1)//2)] + combi[int((n+m -1)//2 + 1)])/2

