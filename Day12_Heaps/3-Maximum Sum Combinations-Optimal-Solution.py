import heapq
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return a list of integers
    import heapq
    def solve(self, A, B, C):
        A.sort()
        B.sort()
        
        n = len(A)
        
        pq = []
        heapq.heapify(pq)
        pq.append((-A[n-1] - B[n-1],(n-1,n-1)))
        my_set = set()
        my_set.add((n-1,n-1))
        
        ans = []
        for count in range(C):
            temp = heapq.heappop(pq)
            
            ans.append(-temp[0])
            
            i = temp[1][0]
            j = temp[1][1]
            s = A[i - 1] + B[j]
            
            temp1 = (i-1,j)
            
            # Insert i-1,j and i,j-1 elements into priority queue
            if temp1 not in my_set:
                heapq.heappush(pq,(-s,temp1))
                my_set.add(temp1)
                
            s = A[i] + B[j - 1]
            temp1 = (i,j-1)
            
            if temp1 not in my_set:
                heapq.heappush(pq,(-s,temp1))
                my_set.add(temp1)
            
        return ans