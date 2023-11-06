def flatten(root):
    #Your code here
    cur = root
    cur2 = root
    l=[]
    
    # Itterating through every node in and storing it in a list , sorting the list and then print the list.
    while cur:
        bot = cur
        bot2 = cur
        while bot:
            l.append(bot.data)
            bot = bot.bottom

        cur = cur.next
        
    l.sort()
    for i in l:
        print(i ,end=" ")