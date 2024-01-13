# TC-O(NlogN) SC-O(N)
def mergeKSortedArrays(kArrays, k:int):
	ans = []
	for i in kArrays:
		ans+=i
	ans.sort()
	return ans