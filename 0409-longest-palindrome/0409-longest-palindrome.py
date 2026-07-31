class Solution:
    def longestPalindrome(self, s: str) -> int:
        dict_s={}
        for i in s:
            if i not in dict_s:
                dict_s[i]=1
            else:
                dict_s[i]+=1
        length=0

        increment=False
        for j in dict_s:
            if dict_s[j]%2==0:
                length+=dict_s[j]
            else:
                increment=True
                length+=(dict_s[j]-1)
        if increment:
            length=length+1
        return length
        