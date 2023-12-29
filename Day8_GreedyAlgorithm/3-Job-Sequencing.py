class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
        
        Jobs.sort(key = lambda x:x.profit,reverse = True)
        
        maxDeadline = -1
        
        for i in range(n):
            maxDeadline = max(maxDeadline,Jobs[i].deadline)
        
        timeLine = [-1] * (maxDeadline+1)
        noJobs = 0
        maxProfit = 0
        
        for i in range(n):
            deadline = Jobs[i].deadline
            for j in range(deadline, 0, -1):
                if timeLine[j] == -1:
                    noJobs+=1
                    timeLine[j] = Jobs[i].id
                    maxProfit+=Jobs[i].profit
                    break
        return noJobs,maxProfit