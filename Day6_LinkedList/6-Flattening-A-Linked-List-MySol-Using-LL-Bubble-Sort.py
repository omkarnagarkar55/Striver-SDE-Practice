def flatten(root):
    #Your code here
    cur = cur2= root
    size = 0
    
    # Flattening the linked list i.e transforming the linked list into a straight line
    while cur:
        bot = cur
        bot2 = cur
        temp = cur.next
        while bot.bottom:

            bot.next = bot.bottom
            size+=1
            bot = bot.bottom
        size+=1
        bot.next = temp
        cur = temp
    
    # Sorting the linked list using Bubble sort
    for _ in range(size):
        pre = cur2
        now = pre.next
        while now:
            if pre.data > now.data:
                pre.data,now.data = now.data,pre.data
            now,pre = now.next,pre.next
    
    # Printing the linked list
    while cur2:
        print(cur2.data ,end=" ")
        cur2 = cur2.next