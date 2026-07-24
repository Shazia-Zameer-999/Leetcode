class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sl=list(s)
        for i in t:
            if i not in sl:
                return i
            if len(sl)!=0:
                sl.remove(i)