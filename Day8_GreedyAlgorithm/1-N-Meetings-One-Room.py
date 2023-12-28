def maximumMeetings(self,n,start,end):
        # code here
        l = []
        meetings = 0
        pre = -1
        # Storing [start ,end and index] in a list.
        for i in range(n):
            l.append([start[i],end[i],i])
            
        #Sorting the list on the end time
        l.sort(key=lambda x: x[1])
        
        # Calculating the number of meetings
        for i in range(n):
            if l[i][0] > pre:
                pre = l[i][1]
                meetings+=1
        return meetings