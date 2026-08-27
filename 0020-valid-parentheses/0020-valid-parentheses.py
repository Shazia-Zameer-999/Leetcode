class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        matching={"{":"}","[":"]","(":")"}
        top=None
        if len(s)%2!=0:
            return False
        for i in s:
            
            if stack:
                top=stack[-1]
            else:
                top=None
            if i in matching:
                stack.append(i)
            else:
                if top!=None and i==matching[top]:
                    stack.pop()
                else:
                    return(False)
        if stack:
            return False
        else:
            return True
