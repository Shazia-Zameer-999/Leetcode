class Solution:
    def reverseVowels(self, s: str) -> str:
        vow=[]
        for i in range(len(s)):
            if s[i] in ["a","e","i","o","u","A","E","I","O","U"]:
                vow.append(i)
        chars=list(s)
        mid=len(vow)//2
        for n in range(mid):
            chars[vow[n]],chars[vow[(len(vow)-1-n)]]=chars[vow[(len(vow)-1-n)]],chars[vow[n]]
        result="".join(chars)
        return result