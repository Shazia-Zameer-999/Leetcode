class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
            }
        total=0
        for i in range(len(s)-1):
            current = roman[s[i].upper()]
            next = roman[s[i+1].upper()]

            if (current>=next):
                total+=current
            else:
                total-=current
        total=total+roman[s[-1].upper()]
        return total