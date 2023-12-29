class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W,arr,n):
        totalValue = 0
        arr.sort(key = lambda x:(x.value/x.weight),reverse = True)
        for item in arr:
            if item.weight <= W:
                totalValue += item.value
                W-=item.weight
            else:
                totalValue += (item.value/item.weight) * W
                W = 0
            if W<=0:
                break
        return totalValue