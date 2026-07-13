class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev=0
        number=x
        while x>0:
            digit=x%10 #123%10= 3 , 12%10=2 , 1%10=1
            rev=rev*10+digit #digit*10^power+rev=300, digit*10+rev=320, digit*1+rev=321
            x=x//10 #123//10=12, 12//10=1 , 1//10=0 (stop loop)
        print(rev)
        if number==rev:
            return True
        else:
            return False

