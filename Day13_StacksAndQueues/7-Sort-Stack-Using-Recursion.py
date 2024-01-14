def sortStack(stack):
    def sortS(stack):
            if len(stack)==0:
                return
            temp = stack.pop()
            sortS(stack)
            insertAtCorrectPos(stack,temp)
    sortS(stack)

def insertAtCorrectPos(stack,temp):
    if len(stack) == 0 or stack[-1] < temp:
        stack.append(temp)
        return
    
    elem = stack.pop()
    insertAtCorrectPos(stack,temp)

    stack.append(elem)
