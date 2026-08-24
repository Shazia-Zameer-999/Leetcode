class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        output=[]
        num=set(nums)
        maximum=len(nums)
        for i in range(1,maximum+1):
            if i not in num:
                output.append(i)
        return output
        