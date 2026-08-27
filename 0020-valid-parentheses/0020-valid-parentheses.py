class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        matching={"{":"}","[":"]","(":")"}
        top=None
        for i in s:
            if len(s)%2!=0:
                return False
            if stack:
                top=stack[-1]
            else:
                top=None
            if i in matching.keys():
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
