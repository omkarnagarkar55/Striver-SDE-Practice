class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        top = -1
        for i in s:
            f= 0
            if i == ')':
                if top!=-1 and stk[top] == '(':
                    f = 1
            elif i == '}':
                if top!=-1 and stk[top] == '{':
                    f = 1
            elif i == ']':
                if top!=-1 and stk[top] == '[':
                    f = 1
            else:
                stk.append(i)
                top += 1
                continue
            
            if f == 1:
                stk.pop()
                top -= 1
            else:
                return False

        if top == -1:
            return True