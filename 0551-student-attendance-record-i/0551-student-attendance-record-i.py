class Solution:
    def checkRecord(self, s: str) -> bool:
        count_A=0
        
        count_L=0
        max_L=0
        for i in s:
            if i=="A":
                count_A+=1
            if count_A>1:
                return False
            if i=="L":
                count_L+=1
            else:
                count_L=0
            if count_L>max_L:
                max_L=count_L
            if max_L>2:
                return False
        return True
        