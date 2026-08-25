class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        maximum=0
        for num in nums:
            if num == 1:
                count += 1
            else:
                count = 0
            if count>maximum:
                maximum=count
        return maximum
