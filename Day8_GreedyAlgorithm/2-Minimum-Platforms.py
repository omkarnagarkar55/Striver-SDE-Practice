class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        # code here
        arr.sort()
        dep.sort()
        
        p = ans = i = 1
        j = 0
        
        while(i<n and j<n):
            
            if arr[i] <= dep[j]:
                p+=1
                i+=1
            elif arr[i] > dep[j]:
                p-=1
                j+=1
            
            if p > ans:
                ans = p
        return ans