class Solution:
    def judgeCircle(self, moves: str) -> bool:
        left=0
        right=0
        up=0
        down=0
        for i in moves:
            if i=="L":
                left+=1
            if i=="R":
                right+=1
            if i=="U":
                up+=1
            if i=="D":
                down+=1
        if left==right and up==down:
            return True
        return False
        