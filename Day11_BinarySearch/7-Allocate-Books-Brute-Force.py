class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
	def books(self, A, B):
        # If number of students are greater than no. of book then return -1
        if B > len(A):
            return -1
        
        # setting low as the max and high as the sum of all pages
        low = max(A)
        high = sum(A)
        
        # Performing linear search for low to high and finding the count of every max pages
        for pages in range(low,high + 1):
            
            if self.countPossibleStudent(A,pages) == B:
                return pages
        return low
    
    def countPossibleStudent(self,arr,pages):
        totalPageCount = 0
        studentCount = 1
        for i in range(len(arr)):
            if totalPageCount + arr[i] <= pages:
                # Adding additional book under same person 
                totalPageCount += arr[i]
            else:
                # moving to the new person
                studentCount+=1
                totalPageCount = arr[i]

        return studentCount