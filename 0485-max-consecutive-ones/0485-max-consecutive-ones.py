class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        output=[]
        for num in nums:
            if num!=1:
                output.append(count)
                count=0
            else:
                count+=1
                output.append(count)
        result=max(output)
        return result
